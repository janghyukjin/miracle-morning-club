class Solution:
    def maxArea(self, height: List[int]) -> int:
        x1, x2 = 0, len(height) -1
        
        maximum = 0

        while x1 < x2:
            y1, y2 = height[x1], height[x2]

            x = x2 - x1
            y = y1 if y1 < y2 else y2

            if maximum < x * y:
                maximum = x * y
            
            if y1 > y2:
                x2 -= 1
            else:
                x1 += 1
        return maximum
            