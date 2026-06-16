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
