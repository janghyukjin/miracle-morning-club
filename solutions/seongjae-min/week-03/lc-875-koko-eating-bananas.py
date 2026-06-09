from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def koko(k: int) -> int:
            count = 0
            for pile in piles:
                count += (pile + k - 1) // k
            return count

        left = 1
        right = max(piles)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            # 빨리 먹고 있을때
            if koko(mid) <= h:
                answer = mid
                right = mid - 1
            # h 시간 안에 다 못먹을 때
            else:
                left = mid + 1

        return answer


# ===== Interview Notes =====
# [Koko Eating Bananas] Medium · Binary Search on Answer
# URL: https://leetcode.com/problems/koko-eating-bananas/
#
# [힌트]
#   - k를 "시간당 먹는 바나나 개수"라고 두고 가능한 최소 k를 찾는다.
#   - k의 범위는 1부터 max(piles)까지.
#   - 어떤 k로 h시간 안에 가능한지 판별하는 helper를 만들어봐.
#
# [체크]
#   - pile 하나를 먹는 시간은 ceil(pile / k).
#   - Python에서는 (pile + k - 1) // k로 올림 나눗셈 가능.
#   - 가능하면 더 작은 k를 찾아야 하므로 right를 줄인다.
# ===== End Interview Notes =====
