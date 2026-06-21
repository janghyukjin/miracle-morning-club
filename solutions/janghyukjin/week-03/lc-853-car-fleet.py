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
