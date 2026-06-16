from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


# ===== Interview Notes =====
# [Sliding Window Maximum] Hard · Monotonic Deque
#
# [접근법]
#   1. Brute force — O(n·k) / O(1)
#      TLE 가능성
#   2. Max heap — O(n log n)
#      lazy deletion
#   3. Monotonic deque (최적) — O(n) / O(k)
#      감소하는 인덱스 큐 유지
#
# [Follow-up 질문 (면접 단골)]
#   - 최소값 버전? (감소 → 증가)
#   - 스트리밍 / 무한 입력?
#   - k가 동적으로 바뀌면?
#
# [Pitfalls / 흔한 실수]
#   - deque에 값 X, 인덱스 O (윈도우 경계 체크용)
#   - 맨 앞 인덱스가 window 밖이면 pop
#
# [최적해 (참고)]
#   from collections import deque
#   dq, res = deque(), []
#   for i, n in enumerate(nums):
#       while dq and nums[dq[-1]] < n: dq.pop()
#       dq.append(i)
#       if dq[0] == i - k: dq.popleft()
#       if i >= k - 1: res.append(nums[dq[0]])
#   return res
# ===== End Interview Notes =====
