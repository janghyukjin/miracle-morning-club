from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = []
        right_to_left = []

        cur = 1
        for num in nums:
            left_to_right.append(cur)
            cur *= num

        cur = 1
        for num in reversed(nums):
            right_to_left.append(cur)
            cur *= num

        right_to_left.reverse()

        result = []
        for i in range(len(nums)):
            result.append(left_to_right[i] * right_to_left[i])

        return result