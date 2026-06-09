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
