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
