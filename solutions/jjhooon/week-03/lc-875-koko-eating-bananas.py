# binary search로 풀어야한다는 것을 알고나서 풀이 성공, 하지만 속도 느림

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def compute_hour(speed):
            hour = 0
            for banana in piles:
                q, r = divmod(banana, speed)
                hour += q
                if r:
                    hour += 1

            return hour

        min_k, max_k = 1, max(piles)
        answer = max_k

        while min_k <= max_k:
            k = (min_k + max_k) // 2

            if compute_hour(k) <= h:
                answer = k
                max_k = k - 1
            else:
                min_k = k + 1
            
        return answer