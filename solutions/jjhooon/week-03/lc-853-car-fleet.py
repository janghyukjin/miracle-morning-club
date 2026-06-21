class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        cars = sorted(zip(position, speed), reverse=True)
        
        answer = 0
        tmp = 0

        for p, s in cars:
            hour = (target - p) / s 
            if tmp < hour:
                answer += 1
                tmp = hour

        return answer
        