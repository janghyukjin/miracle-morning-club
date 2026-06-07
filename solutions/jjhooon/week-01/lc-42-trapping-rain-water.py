class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        answer = 0
        lwater, rwater = 0, 0

        while left < right:
            if height[left] < height[right]:
                lwater = max(lwater, height[left])
                answer += (lwater - height[left]) 
                left += 1
            else:
                rwater = max(rwater, height[right])
                answer += (rwater - height[right])
                right -= 1

        return answer


# ===== Interview Notes =====
# [Trapping Rain Water] Hard · Two Pointers / DP / Stack
#
# [접근법]
#   1. DP (prefix max) — O(n) / O(n)
#      leftMax[i], rightMax[i] 미리 계산
#   2. Two pointers (최적) — O(n) / O(1)
#      짧은 쪽 max로 contribution 계산
#   3. Monotonic stack — O(n) / O(n)
#      감소 스택, 면 단위 계산
#
# [Follow-up 질문 (면접 단골)]
#   - 2D 버전은? (LC 407, BFS+priority queue)
#   - 스트리밍 입력에서?
#   - 스택 풀이 vs 투포인터 트레이드오프?
#
# [Pitfalls / 흔한 실수]
#   - 양 끝은 항상 0
#   - min(leftMax, rightMax) - height[i] 음수 가능
#
# [최적해 (참고)]
#   l, r = 0, len(height) - 1
#   lMax = rMax = ans = 0
#   while l < r:
#       if height[l] < height[r]:
#           lMax = max(lMax, height[l])
#           ans += lMax - height[l]
#           l += 1
#       else:
#           rMax = max(rMax, height[r])
#           ans += rMax - height[r]
#           r -= 1
#   return ans
# ===== End Interview Notes =====
