from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        res = max(piles)
        left = 1
        right = max(piles)
        while left <= right:
            cnt = 0
            tmp = (left + right) // 2
            for pile in piles:
                moc = pile // tmp
                remain = pile % tmp
                cnt += moc
                if remain > 0:
                    cnt += 1
            if cnt <= h:
                res = min(res, tmp)
                right = tmp - 1
            else:
                left = tmp + 1
        return res


# ===== Interview Notes =====
# [Koko Eating Bananas] Medium · Parametric Binary Search
#
# [접근법]
#   1. Parametric Binary Search on answer — O(n log M) / O(1)   ← 본인 풀이
#      - 탐색 대상이 "배열의 인덱스"가 아니라 "정답값(먹는 속도 k)" 자체.
#      - k에 대해 "h시간 안에 다 먹을 수 있는가?" 는 단조(monotonic):
#        k가 크면 항상 가능, 작으면 불가능 → 이분 탐색 적용 가능.
#      - 가능한 최소 k를 찾는 lower_bound 패턴.
#   2. Brute force — O(n * M), M = max(piles)
#      k=1부터 차례로 시도. n,M이 크면 TLE.
#
# [핵심 아이디어 — Parametric Search]
#   - "답을 직접 구하기 어렵지만, 답 후보를 주면 가능/불가능 판정은 쉽다"
#     → 정답값 자체를 이분 탐색.
#   - 판정 함수 (k, h): sum(ceil(pile / k) for pile in piles) <= h
#   - 단조성 보장: k↑ → 필요 시간↓ (정렬된 boolean 시퀀스 FFFF...TTTT)
#
# [본인 풀이 분석]
#   - `piles.sort()` 는 사실 불필요 (이 문제에선 순서 영향 없음). 빼도 정답.
#   - `res = max(piles)` 초기화로 시작값을 안전하게 잡은 점은 좋음.
#   - moc/remain 으로 ceil 구현: ceil(a/b) = a//b + (1 if a%b else 0). 정확함.
#   - left <= right + res 갱신 패턴 → lower_bound와 동치. OK.
#
# [Follow-up 질문 (면접 단골)]
#   - sort가 왜 필요했어? → 사실 필요 없음. 빼는 게 더 좋음 (O(n log n) 제거).
#   - ceil을 더 깔끔하게? → `-(-pile // k)` 또는 `(pile + k - 1) // k`.
#   - right 초기값을 max(piles) 로 잡은 이유? → 어떤 pile이든 1시간에 다 먹는 속도
#     가 max(piles)이므로 그게 정답의 상한.
#   - 만약 piles 길이가 매우 커서 sum 계산도 느리면? → prefix sum / 분할 정복은
#     이 문제 구조상 의미 없음. 핵심은 이분 탐색 자체.
#   - 변형 — LC 1011 (Capacity to Ship Packages), LC 410 (Split Array Largest Sum)
#     모두 동일한 "정답값에 대한 이분 탐색" 패턴.
#
# [Pitfalls / 흔한 실수]
#   - k = 0 후보를 포함시키면 ZeroDivisionError → 시작값 1.
#   - ceil을 `pile // k + 1` 로 잘못 적기 (정확히 나눠떨어지는 케이스 오버카운트).
#   - h <= len(piles) 인데도 답이 항상 존재하는 걸 안 깨닫고 edge 처리 추가 (불필요).
#   - "정답이 단조"임을 못 알아채고 brute force.
#
# [복잡도]
#   - Time:  O(n log M),  M = max(piles)
#   - Space: O(1)  (정렬 제거 시. 본인 풀이는 sort 때문에 O(log n) 또는 O(n))
#
# [최적해 (참고) — sort 제거 + 깔끔한 ceil + 표준 lower_bound]
#   def minEatingSpeed(piles, h):
#       lo, hi = 1, max(piles)
#       while lo < hi:
#           k = (lo + hi) // 2
#           if sum(-(-p // k) for p in piles) <= h:
#               hi = k
#           else:
#               lo = k + 1
#       return lo
# ===== End Interview Notes =====
