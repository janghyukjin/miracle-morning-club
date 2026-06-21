from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2

        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2
            j = half - i
            Aleft = float("-inf") if i == 0 else A[i - 1]
            Aright = float("inf") if i == len(A) else A[i]

            Bleft = float("-inf") if j == 0 else B[j - 1]
            Bright = float("inf") if j == len(B) else B[j]
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


# ===== Interview Notes =====
# [Median of Two Sorted Arrays] Hard · Binary Search Partition
# 제약: O(log min(m,n)) time required
#
# [접근법]
#   1. Merge & sort — O(m+n)
#      요건 못 맞춤
#   2. Binary search partition (최적) — O(log min(m,n))
#      짧은 쪽에서 partition
#
# [Follow-up 질문 (면접 단골)]
#   - k-th smallest 일반화?
#   - K개 배열의 median?
#   - 스트리밍 (LC 295)?
#
# [Pitfalls / 흔한 실수]
#   - 빈 배열, 한쪽이 모두 작거나 큰 경우
#   - odd/even total 처리
#   - partition 인덱스 inf 처리
#
# [최적해 (참고)]
#   if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
#   m, n = len(nums1), len(nums2)
#   total = m + n
#   l, r = 0, m
#   while l <= r:
#       i = (l + r) // 2
#       j = (total + 1) // 2 - i
#       L1 = nums1[i-1] if i > 0 else float('-inf')
#       R1 = nums1[i] if i < m else float('inf')
#       L2 = nums2[j-1] if j > 0 else float('-inf')
#       R2 = nums2[j] if j < n else float('inf')
#       if L1 <= R2 and L2 <= R1:
#           if total % 2: return max(L1, L2)
#           return (max(L1, L2) + min(R1, R2)) / 2
#       elif L1 > R2: r = i - 1
#       else: l = i + 1
# ===== End Interview Notes =====
