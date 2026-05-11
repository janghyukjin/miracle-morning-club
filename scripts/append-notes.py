#!/usr/bin/env python3
"""
LeetCode 풀이 파일에 정적 면접 노트(data/lc-notes.json) 자동 append.

- solutions/**/lc-*.py 같은 파일 찾기
- 파일명에서 LC 번호 추출 → data/lc-notes.json에서 노트 조회
- 이미 노트 있는 파일은 건너뜀 (idempotent)
- 코드 주석으로 파일 끝에 append

API 호출 없음. 무료. NeetCode 150 Phase 1 (Week 1-4) 커버.
"""

import json
import os
import re
import sys
import glob
from pathlib import Path

MARKER_START = "===== Interview Notes ====="
MARKER_END = "===== End Interview Notes ====="
NOTES_DB_PATH = "data/lc-notes.json"

# 파일 확장자 → 주석 prefix
COMMENT_STYLES = {
    ".py": "#",
    ".js": "//",
    ".ts": "//",
    ".go": "//",
    ".java": "//",
    ".cpp": "//",
    ".c": "//",
    ".rs": "//",
    ".kt": "//",
    ".swift": "//",
}


def load_notes_db():
    """data/lc-notes.json 로드."""
    try:
        with open(NOTES_DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"✗ Notes DB not found: {NOTES_DB_PATH}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"✗ Notes DB JSON parse error: {e}", file=sys.stderr)
        sys.exit(1)


def extract_lc_number(filepath):
    """파일명에서 LC 번호 추출. 'lc-49-group-anagrams.py' → '49'."""
    fname = os.path.basename(filepath)
    m = re.match(r"^lc-(\w+)-.+\.\w+$", fname)
    return m.group(1) if m else None


def has_marker(content, comment_prefix):
    """이미 노트 있는지 (idempotent)."""
    return f"{comment_prefix} {MARKER_START}" in content


def format_note(note_data):
    """노트 dict → 사람이 읽기 좋은 텍스트."""
    lines = []
    lines.append(f"[{note_data['title']}] {note_data.get('difficulty', '')} · {note_data.get('pattern', '')}")

    if note_data.get("constraints"):
        lines.append(f"제약: {note_data['constraints']}")

    lines.append("")
    lines.append("[접근법]")
    for i, ap in enumerate(note_data.get("approaches", []), 1):
        lines.append(f"  {i}. {ap['name']} — {ap['complexity']}")
        if ap.get("note"):
            lines.append(f"     {ap['note']}")

    if note_data.get("followups"):
        lines.append("")
        lines.append("[Follow-up 질문 (면접 단골)]")
        for q in note_data["followups"]:
            lines.append(f"  - {q}")

    if note_data.get("pitfalls"):
        lines.append("")
        lines.append("[Pitfalls / 흔한 실수]")
        for p in note_data["pitfalls"]:
            lines.append(f"  - {p}")

    if note_data.get("optimal_code"):
        lines.append("")
        lines.append("[최적해 (참고)]")
        for code_line in note_data["optimal_code"].split("\n"):
            lines.append(f"  {code_line}")

    return "\n".join(lines)


def append_notes(filepath, note_text, comment_prefix):
    """노트를 코드 주석으로 wrap해서 파일 끝에 append."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if has_marker(content, comment_prefix):
        return False

    lines = [f"{comment_prefix} {MARKER_START}"]
    for line in note_text.split("\n"):
        if line.strip():
            lines.append(f"{comment_prefix} {line}")
        else:
            lines.append(comment_prefix)
    lines.append(f"{comment_prefix} {MARKER_END}")

    # 파일 끝 줄바꿈 정규화
    separator = "\n\n" if content.endswith("\n") else "\n\n\n"
    new_content = content + separator + "\n".join(lines) + "\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    notes_db = load_notes_db()
    print(f"📚 Loaded notes DB ({len(notes_db) - 1} problems)\n")

    success = 0
    skipped = 0
    no_note = 0

    for ext, comment in COMMENT_STYLES.items():
        for filepath in glob.glob(f"solutions/**/lc-*{ext}", recursive=True):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except OSError as e:
                print(f"  ⚠ Could not read {filepath}: {e}", file=sys.stderr)
                continue

            if has_marker(content, comment):
                skipped += 1
                continue

            lc_num = extract_lc_number(filepath)
            if not lc_num:
                print(f"  ⚠ Invalid filename: {filepath}")
                continue

            if lc_num not in notes_db:
                print(f"  ℹ LC {lc_num}: 노트 DB에 없음 ({filepath})")
                no_note += 1
                continue

            note_text = format_note(notes_db[lc_num])
            if append_notes(filepath, note_text, comment):
                print(f"  ✓ LC {lc_num}: {filepath}")
                success += 1

    print("")
    print(f"✓ Added: {success}")
    print(f"⏭  Skipped (already noted): {skipped}")
    print(f"ℹ  No note in DB: {no_note}")


if __name__ == "__main__":
    main()
