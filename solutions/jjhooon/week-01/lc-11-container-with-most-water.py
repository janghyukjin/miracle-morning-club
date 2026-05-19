class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = -float(inf)

        while i < j:
            if height[i] > height[j]:
                area = (j-i) * height[j]
                j -= 1
            else:
                area = (j-i) * height[i]
                i += 1
                
            max_area = max(max_area, area)

        return max_area