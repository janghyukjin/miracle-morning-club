class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten = []
        for row in matrix:
            for num in row:
                flatten.append(num)

        left, right = 0, len(flatten) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if flatten[middle] == target:
                return True
            elif flatten[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False