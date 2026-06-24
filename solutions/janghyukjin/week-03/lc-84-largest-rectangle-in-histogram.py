from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                res = max(res, h * width)
            stack.append(i)
        return res


# ===== Interview Notes =====
# [Largest Rectangle in Histogram] Hard · Monotonic Stack
#
# [접근법]
#   1. Brute force — O(n²)
#      각 bar 기준 좌우 확장
#   2. Monotonic stack (최적) — O(n) / O(n)
#      증가 스택, pop 시 면적 계산
#
# [Follow-up 질문 (면접 단골)]
#   - Maximal Rectangle (LC 85, 2D)?
#   - k개 막대 중 최대?
#   - 스트리밍?
#
# [Pitfalls / 흔한 실수]
#   - sentinel 0 추가 (마지막 처리)
#   - popping 시 width 계산 (i - stack[-1] - 1)
#
# [최적해 (참고)]
#   stack, best = [], 0
#   heights.append(0)  # sentinel
#   for i, h in enumerate(heights):
#       while stack and heights[stack[-1]] > h:
#           top = stack.pop()
#           width = i if not stack else i - stack[-1] - 1
#           best = max(best, heights[top] * width)
#       stack.append(i)
#   heights.pop()
#   return best
# ===== End Interview Notes =====
