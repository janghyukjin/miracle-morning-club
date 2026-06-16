from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        res = []

        def make(arr, left_cnt, right_cnt):
            if left_cnt == right_cnt == n:
                res.append("".join(arr))
                return
            if left_cnt < n:
                arr.append("(")
                make(arr, left_cnt + 1, right_cnt)
                arr.pop()
            if left_cnt > right_cnt:
                arr.append(")")
                make(arr, left_cnt, right_cnt + 1)
                arr.pop()

        make(arr, 0, 0)
        return res


# ===== Interview Notes =====
# [Generate Parentheses] Medium · Backtracking / DFS
#
# [접근법]
#   1. Backtracking — O(4ⁿ/√n) Catalan / O(n) recursion
#      open/close 카운트 추적
#   2. DP (Catalan) — O(4ⁿ/√n)
#      n-1에서 빌드
#
# [Follow-up 질문 (면접 단골)]
#   - ()[]{} 모두 사용한다면?
#   - 개수만 (실제 문자열 X)? (Catalan number)
#   - 특정 valid 패턴 매칭?
#
# [Pitfalls / 흔한 실수]
#   - close > open일 때 가지치기
#   - open <= n 조건
#
# [최적해 (참고)]
#   res = []
#   def bt(cur, opn, cls):
#       if len(cur) == 2 * n:
#           res.append(cur); return
#       if opn < n: bt(cur + '(', opn + 1, cls)
#       if cls < opn: bt(cur + ')', opn, cls + 1)
#   bt('', 0, 0)
#   return res
# ===== End Interview Notes =====
