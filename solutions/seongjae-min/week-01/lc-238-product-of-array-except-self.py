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


# ===== Interview Notes =====
# [Product of Array Except Self] Medium · Prefix/Suffix Product
# 제약: 나눗셈 금지, O(n) time
#
# [접근법]
#   1. Prefix + Suffix 배열 — O(n) / O(n)
#      left[i] × right[i]
#   2. In-place (최적) — O(n) / O(1) excl. output
#      결과 배열에 prefix 채우고 suffix는 변수로
#
# [Follow-up 질문 (면접 단골)]
#   - 결과 배열 외 O(1) space?
#   - 나눗셈 허용하면? (0 처리 주의)
#   - 2D 배열로 확장하면?
#
# [Pitfalls / 흔한 실수]
#   - 0이 1개일 때 (해당 위치만 nonzero product)
#   - 0이 2개 이상일 때 (모두 0)
#   - Integer overflow (Python은 OK, Java/C++ 주의)
#
# [최적해 (참고)]
#   n = len(nums)
#   res = [1] * n
#   for i in range(1, n):
#       res[i] = res[i-1] * nums[i-1]
#   right = 1
#   for i in range(n-1, -1, -1):
#       res[i] *= right
#       right *= nums[i]
#   return res
# ===== End Interview Notes =====
