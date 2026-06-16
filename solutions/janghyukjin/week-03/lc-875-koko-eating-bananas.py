from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        left = 1
        right = max(piles)
        while left <= right:
            cnt = 0
            tmp = (left + right) // 2
            for pile in piles:
                cnt += (pile + tmp - 1) // tmp
                if cnt > h:
                    break
            if cnt <= h:
                res = min(res, tmp)
                right = tmp - 1
            else:
                left = tmp + 1
        return res


# ===== Interview Notes =====
# [Koko Eating Bananas] Medium · Binary Search on Answer
#
# [접근법]
#   1. Binary search speed — O(n log max(piles))
#      속도 1~max, feasible 체크
#
# [Follow-up 질문 (면접 단골)]
#   - 여러 마리 (multiple workers)?
#   - 휴식 시간 있으면?
#   - speed가 정수 아닐 때?
#
# [Pitfalls / 흔한 실수]
#   - ceil division: (pile + k - 1) // k 또는 math.ceil(pile / k)
#   - l = 1 (0은 의미 없음)
#   - r = max(piles) (그 이상은 의미 없음)
#
# [최적해 (참고)]
#   l, r = 1, max(piles)
#   while l < r:
#       mid = (l + r) // 2
#       if sum((p + mid - 1) // mid for p in piles) <= h: r = mid
#       else: l = mid + 1
#   return l
# ===== End Interview Notes =====
