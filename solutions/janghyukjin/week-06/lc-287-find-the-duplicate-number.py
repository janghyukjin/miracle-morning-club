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


# ===== Interview Notes =====
# [Find the Duplicate Number] Medium · Floyd's Cycle Detection / Binary Search
# 제약: O(1) space, no modification
#
# [접근법]
#   1. Floyd's Tortoise and Hare — O(n) / O(1)
#      배열을 linked list로 해석
#   2. Binary search on value — O(n log n) / O(1)
#      <=mid인 개수 카운트
#   3. Hash set — O(n) / O(n)
#      공간 제약 위반
#
# [Follow-up 질문 (면접 단골)]
#   - 여러 duplicate 모두 찾기?
#   - 중복 횟수까지?
#   - 수정 허용되면 더 간단? (sort, mark negative)
#
# [Pitfalls / 흔한 실수]
#   - phase 1 (만남)과 phase 2 (사이클 시작점) 구분
#   - 값이 [1, n] 범위라는 점 활용
#
# [최적해 (참고)]
#   # Floyd's
#   slow = fast = nums[0]
#   while True:
#       slow = nums[slow]
#       fast = nums[nums[fast]]
#       if slow == fast: break
#   slow = nums[0]
#   while slow != fast:
#       slow = nums[slow]
#       fast = nums[fast]
#   return slow
# ===== End Interview Notes =====
