from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maximum = 0
        while l < r:
            minimum = min(height[l], height[r])
            water = (r - l) * minimum
            maximum = max(maximum, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maximum


# ===== Interview Notes =====
# [Container With Most Water] Medium · Two Pointers
#
# [접근법]
#   1. Brute force — O(n²) / O(1)
#      모든 쌍 시도
#   2. Two pointers (최적) — O(n) / O(1)
#      양 끝에서 시작, 짧은 쪽 이동
#
# [Follow-up 질문 (면접 단골)]
#   - 왜 짧은 쪽을 움직이나? (긴 쪽 움직이면 area 절대 안 늘어남)
#   - 여러 컨테이너의 합? (LC 42)
#   - 3D 또는 가중치 있으면?
#
# [Pitfalls / 흔한 실수]
#   - 긴 쪽 움직이면 답 누락
#   - 두 높이 같을 때 양쪽 다 시도 가능
#
# [최적해 (참고)]
#   l, r, best = 0, len(height) - 1, 0
#   while l < r:
#       best = max(best, min(height[l], height[r]) * (r - l))
#       if height[l] < height[r]: l += 1
#       else: r -= 1
#   return best
# ===== End Interview Notes =====
