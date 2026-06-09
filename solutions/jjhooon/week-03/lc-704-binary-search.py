class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle

            elif nums[middle] > target:
                right = middle - 1
                
            else:
                left = middle + 1 
                
        return -1


# ===== Interview Notes =====
# [Binary Search] Easy · Binary Search (foundation)
#
# [접근법]
#   1. Standard binary search — O(log n) / O(1)
#
# [Follow-up 질문 (면접 단골)]
#   - 첫번째/마지막 occurrence는? (lower/upper bound)
#   - 회전된 배열에서? (LC 33)
#   - 답의 범위에 대한 binary search? (LC 875)
#
# [Pitfalls / 흔한 실수]
#   - mid = (l+r)//2 → 큰 수에서 overflow (l + (r-l)//2 권장)
#   - <=, < 경계 실수
#   - l = mid+1, r = mid-1 (무한 루프 방지)
#
# [최적해 (참고)]
#   l, r = 0, len(nums) - 1
#   while l <= r:
#       mid = l + (r - l) // 2
#       if nums[mid] == target: return mid
#       elif nums[mid] < target: l = mid + 1
#       else: r = mid - 1
#   return -1
# ===== End Interview Notes =====
