from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # phase 1: 만날 때까지 (slow 1칸, fast 2칸)
        left = 0
        right = 0
        while True:
            left = nums[left]
            right = nums[nums[right]]
            if left == right:
                break

        # phase 2: 한쪽을 0으로 리셋, 같은 속도로 진입점까지
        left = 0
        while left != right:
            left = nums[left]
            right = nums[right]

        return left
