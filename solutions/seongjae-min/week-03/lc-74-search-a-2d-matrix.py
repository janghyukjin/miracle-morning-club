from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for row in matrix:
            for x in row:
                flat.append(x)
        
        left = 0
        right = len(flat) - 1

        while left <= right:
            mid = (left + right) // 2

            if flat[mid] == target:
                return True
            elif flat[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


# ===== Interview Notes =====
# [Search a 2D Matrix] Medium · Binary Search
# URL: https://leetcode.com/problems/search-a-2d-matrix/
#
# [힌트]
#   - m*n 길이의 1D sorted array처럼 생각할 수 있다.
#   - index i를 row = i // n, col = i % n으로 변환.
#   - 또는 먼저 row를 찾고 그 row 안에서 binary search.
#
# [체크]
#   - m, n 계산.
#   - left=0, right=m*n-1로 시작.
#   - matrix[mid // n][mid % n] 접근이 핵심.
# ===== End Interview Notes =====
