#!/usr/bin/env python3
"""
LeetCode 풀이 파일에 Claude AI 면접 분석 노트를 자동 append.

- solutions/**/lc-*.py 같은 파일 찾기
- 이미 노트 있는 파일은 건너뜀 (idempotent)
- Anthropic API 호출 → 풀이 평가 + 최적해 + Follow-up + Pitfalls
- 파일 끝에 코드 주석으로 append
"""

import os
import re
import sys
import glob

from anthropic import Anthropic

MODEL = "claude-sonnet-4-6"
MARKER_START = "===== Interview Notes (AI-generated) ====="
MARKER_END = "===== End Interview Notes ====="

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

SYSTEM_PROMPT = """당신은 한국 소프트웨어 엔지니어가 FAANG급 코딩 인터뷰를 준비하도록 돕는 코칭 전문가입니다.

제출된 LeetCode 풀이를 분석하여 다음 4섹션을 한국어로 제공하세요:

[풀이 평가]
- 시간/공간 복잡도
- 접근 방법 평가 (간결하게)

[최적해]
- 더 빠른 풀이가 있으면 코드와 함께 제시 (들여쓰기 깔끔하게)
- 이미 최적이면 "이미 최적입니다" 한 줄

[Follow-up 질문 3개]
- 면접관이 물을 만한 후속 질문 정확히 3개

[Pitfalls]
- 흔한 실수 / 엣지 케이스 2-3개

규칙:
- 평문 한국어. 마크다운 헤더(#) X, 코드 펜스(```) X
- 코드는 들여쓰기로 표현. 본문은 자유롭게
- 전체 길이 400~700자
- 각 섹션은 [] 헤더로 구분
- 본인 풀이가 이미 최적이면 솔직히 인정 (억지로 다른 방법 제시 X)"""


def extract_lc_meta(filepath):
    """파일명에서 LC 번호 + slug 추출."""
    fname = os.path.basename(filepath)
    m = re.match(r"^lc-(\w+)-(.+)\.(\w+)$", fname)
    if not m:
        return None
    return {
        "number": m.group(1),
        "slug": m.group(2),
        "name": m.group(2).replace("-", " ").title(),
        "ext": "." + m.group(3),
    }


def has_marker(content, comment_prefix):
    """이미 노트 있는지 확인 (idempotent)."""
    return f"{comment_prefix} {MARKER_START}" in content


def find_unmarked_files():
    """노트 없는 풀이 파일 모두 찾기."""
    files = []
    for ext, comment in COMMENT_STYLES.items():
        for path in glob.glob(f"solutions/**/lc-*{ext}", recursive=True):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if not has_marker(content, comment):
                    files.append(path)
            except OSError as e:
                print(f"  ⚠ Could not read {path}: {e}", file=sys.stderr)
    return files


def analyze_solution(client, code, lc_meta):
    """Claude API 호출하여 풀이 분석."""
    user_msg = f"""LeetCode {lc_meta['number']} — {lc_meta['name']}
URL: https://leetcode.com/problems/{lc_meta['slug']}/

내 풀이:
```
{code}
```

위 풀이를 분석해주세요."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    return response.content[0].text.strip()


def append_notes(filepath, notes, comment_prefix):
    """노트를 코드 주석으로 wrap해서 파일 끝에 append."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if has_marker(content, comment_prefix):
        return False

    lines = [f"{comment_prefix} {MARKER_START}"]
    for line in notes.split("\n"):
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
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(
            "✗ ANTHROPIC_API_KEY not set. "
            "Add it at Settings → Secrets and variables → Actions.",
            file=sys.stderr,
        )
        sys.exit(0)  # 워크플로 실패시키지 않음

    client = Anthropic(api_key=api_key)
    unmarked = find_unmarked_files()

    if not unmarked:
        print("✓ All solution files already have notes. Nothing to do.")
        return

    print(f"📝 Found {len(unmarked)} file(s) needing notes\n")

    success = 0
    for filepath in unmarked:
        lc_meta = extract_lc_meta(filepath)
        if not lc_meta:
            print(f"  ⚠ Skipping (invalid filename): {filepath}")
            continue

        comment = COMMENT_STYLES.get(lc_meta["ext"])
        if not comment:
            continue

        print(f"  → LC {lc_meta['number']} ({lc_meta['name']}): analyzing...")

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read()
            notes = analyze_solution(client, code, lc_meta)
            if append_notes(filepath, notes, comment):
                print(f"    ✓ Added notes to {filepath}\n")
                success += 1
        except Exception as e:
            print(f"    ✗ Failed: {e}\n", file=sys.stderr)

    print(f"\n✓ Successfully processed {success}/{len(unmarked)} files")


if __name__ == "__main__":
    main()
