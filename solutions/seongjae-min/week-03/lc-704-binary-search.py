from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# ===== Interview Notes =====
# [Binary Search] Easy · Binary Search
# URL: https://leetcode.com/problems/binary-search/
#
# [힌트]
#   - left, right를 inclusive로 둘지 exclusive로 둘지 먼저 정해.
#   - mid 계산 후 nums[mid]와 target 비교.
#   - 못 찾으면 -1.
#
# [체크]
#   - while 조건이 left <= right인지 left < right인지 일관성 유지.
#   - left/right 업데이트에서 mid를 다시 포함시키지 않기.
#   - 빈 배열은 LeetCode 제약 밖이지만 처리해도 좋음.
# ===== End Interview Notes =====
