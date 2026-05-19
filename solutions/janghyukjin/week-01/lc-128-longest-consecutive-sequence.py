from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        for num in numSet:
            left = count.get(num - 1, 0)
            right = count.get(num + 1, 0)
            length = left + right + 1

            count[num] = length

            start = num - left
            end = num + right
            for x in range(start, end + 1):
                count[x] = length

        result = max(count.values())
        return result
