from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# ===== Interview Notes =====
# [Find Minimum in Rotated Sorted Array] Medium · Binary Search
#
# [접근법]
#   1. Compare with right — O(log n)
#      nums[mid] > nums[r]면 min은 오른쪽
#
# [Follow-up 질문 (면접 단골)]
#   - 중복 있으면? (LC 154, worst O(n))
#   - 회전 횟수는?
#   - 특정 값 찾기 (LC 33)?
#
# [Pitfalls / 흔한 실수]
#   - 회전 안 된 경우 (정렬됨, l 반환)
#   - nums[mid]와 nums[l] 비교는 X (애매함)
#
# [최적해 (참고)]
#   l, r = 0, len(nums) - 1
#   while l < r:
#       mid = (l + r) // 2
#       if nums[mid] > nums[r]: l = mid + 1
#       else: r = mid
#   return nums[l]
# ===== End Interview Notes =====
