# 📝 Interview Notes (Auto-append)

본인이 풀이 push하면 GitHub Action이 자동으로 `data/lc-notes.json`을 조회해서
파일 끝에 면접 노트를 주석으로 추가합니다.

## 작동 방식

```
[당신] git push solutions/janghyukjin/week-01/lc-49-group-anagrams.py
   ↓
[GitHub Action] 파일 감지 → data/lc-notes.json에서 LC 49 노트 조회
   ↓
[Action] 파일 끝에 주석으로 노트 append → 자동 commit + push
   ↓
[당신] git pull 하면 노트 추가된 파일 받음
```

## 노트 형식

각 풀이 파일 끝에 이런 식으로 붙음:

```python
class Solution:
    def groupAnagrams(self, strs):
        # ... 본인 풀이 ...

# ===== Interview Notes =====
# [Group Anagrams] Medium · Hash Map + Sorting/Counting
#
# [접근법]
#   1. Sorted tuple key — O(n·k log k) / O(n·k)
#      tuple(sorted(s))를 dict key로
#   2. Character count key (optimal) — O(n·k) / O(n·k)
#      [0]*26 카운트 배열을 tuple로
#
# [Follow-up 질문 (면접 단골)]
#   - sort 없이 풀 수 있나? (→ char count)
#   - k(문자열 길이)가 매우 크면?
#   - Unicode/non-ASCII 처리는?
#
# [Pitfalls / 흔한 실수]
#   - list는 hashable 아님 → tuple로 변환
#   - 대소문자 구분 (Abc vs abc)
#
# [최적해 (참고)]
#   from collections import defaultdict
#   d = defaultdict(list)
#   for s in strs:
#       cnt = [0] * 26
#       for c in s: cnt[ord(c) - ord('a')] += 1
#       d[tuple(cnt)].append(s)
#   return list(d.values())
# ===== End Interview Notes =====
```

## 셋업

**셋업 불필요!** API 키, 토큰, 비용 모두 X. 자동 작동.

## 커버리지

현재 노트 DB는 **NeetCode 150 Phase 1 (Week 1-4) = 29문제** 포함:

- Week 1: Arrays & Hashing (LC 49, 347, 238, 271, 128, 11, 42)
- Week 2: Sliding Window + Stack (LC 3, 424, 567, 76, 239, 155, 22)
- Week 3: Binary Search + Stack (LC 704, 74, 875, 153, 33, 4, 853, 84)
- Week 4: Linked List (LC 143, 138, 2, 287, 146, 23, 25)

→ Week 5+는 추후 추가 예정. 노트 없는 LC는 그냥 풀이만 남음.

## 노트 DB 확장 (Week 5+ 추가하려면)

`data/lc-notes.json`에 새 항목 추가:

```json
{
  "226": {
    "title": "Invert Binary Tree",
    "difficulty": "Easy",
    "pattern": "Tree DFS/BFS",
    "approaches": [
      {"name": "Recursive", "complexity": "O(n) / O(h)", "note": "left/right 교환"}
    ],
    "followups": ["iterative로?", "BFS로?", "verify 함수는?"],
    "pitfalls": ["null 체크"],
    "optimal_code": "if not root: return None\nroot.left, root.right = self.invertTree(root.right), self.invertTree(root.left)\nreturn root"
  }
}
```

push하면 Action이 자동으로 기존 풀이까지 백필.

## 노트 다시 받기 (재분석)

파일에서 `===== Interview Notes` ~ `===== End Interview Notes` 블록을
지우고 push하면 새로 받음.

## 무한 루프 방지

Action의 자동 commit은 `[skip notes]` 태그가 있어 자기 자신을 재트리거하지 않음.

## 향후: AI 분석 추가 옵션

만약 본인 코드를 AI가 분석해서 개인화된 피드백을 받고 싶으면:
1. Anthropic API 계정 추가 ($5 충전)
2. `ANTHROPIC_API_KEY`를 GitHub Secret으로 등록
3. 스크립트를 AI 분석 버전으로 교체

지금은 정적 노트로도 충분히 면접 준비 가능. AI는 over-engineering.
