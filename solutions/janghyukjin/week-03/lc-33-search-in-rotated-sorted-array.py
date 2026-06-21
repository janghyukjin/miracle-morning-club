from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


# ===== Interview Notes =====
# [Search in Rotated Sorted Array] Medium · Binary Search (partition-aware)
#
# [접근법]
#   1. 단일 binary search — O(log n)
#      정렬된 half 식별 → target 어디?
#   2. pivot 찾고 이진 탐색 — O(log n)
#      LC 153 + LC 704 조합
#
# [Follow-up 질문 (면접 단골)]
#   - 중복 있으면? (LC 81, worst O(n))
#   - 회전 인덱스도 같이 반환?
#   - 회전 안 된 경우 처리?
#
# [Pitfalls / 흔한 실수]
#   - nums[mid] >= nums[l] (등호 포함 — l과 mid 같은 위치 가능)
#   - target이 범위 안에 있는지 정확히 체크
#
# [최적해 (참고)]
#   l, r = 0, len(nums) - 1
#   while l <= r:
#       mid = (l + r) // 2
#       if nums[mid] == target: return mid
#       if nums[l] <= nums[mid]:  # 왼쪽 정렬
#           if nums[l] <= target < nums[mid]: r = mid - 1
#           else: l = mid + 1
#       else:  # 오른쪽 정렬
#           if nums[mid] < target <= nums[r]: l = mid + 1
#           else: r = mid - 1
#   return -1
# ===== End Interview Notes =====
