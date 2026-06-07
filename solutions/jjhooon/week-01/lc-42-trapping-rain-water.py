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