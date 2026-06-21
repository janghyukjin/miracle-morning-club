from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        prev = 0
        for p, s in cars:
            time = (target - p) / s
            if prev < time:
                res += 1
                prev = time
        return res


# ===== Interview Notes =====
# [Car Fleet] Medium · Sort + Stack (or simulation)
#
# [접근법]
#   1. Sort by position desc, stack/time tracking — O(n log n)
#      더 빠른 차가 앞 차 따라잡으면 fleet 합쳐짐
#
# [Follow-up 질문 (면접 단골)]
#   - 양방향 (반대편에서 오는 차)?
#   - 충돌 시 멈춤이면?
#   - 여러 lane?
#
# [Pitfalls / 흔한 실수]
#   - time = (target - pos) / speed (float)
#   - 내림차순 정렬 + 뒤에서부터 보면서 max time 유지
#
# [최적해 (참고)]
#   cars = sorted(zip(position, speed), reverse=True)
#   stack = []
#   for pos, spd in cars:
#       t = (target - pos) / spd
#       if not stack or t > stack[-1]:
#           stack.append(t)
#   return len(stack)
# ===== End Interview Notes =====
