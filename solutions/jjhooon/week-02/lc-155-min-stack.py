class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack:
            self.minStack.append(value)
        else:
            self.minStack.append(min(value, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# ===== Interview Notes =====
# [Min Stack] Medium · Stack Design
#
# [접근법]
#   1. Two stacks — O(1) all ops / O(n)
#      값 스택 + min 스택
#   2. Single stack with (val, min) — O(1) / O(n)
#      각 entry에 min도 저장
#   3. Encoded diff (공간 최적) — O(1) / O(n)
#      min - val 인코딩, 복잡
#
# [Follow-up 질문 (면접 단골)]
#   - Max도 같이 (Max-Min Stack)?
#   - Queue 버전 (LC 225/232 응용)?
#   - Median Stack?
#
# [Pitfalls / 흔한 실수]
#   - pop할 때 min 스택도 정확히 갱신
#   - 빈 스택 처리
#
# [최적해 (참고)]
#   class MinStack:
#       def __init__(self):
#           self.stack, self.mins = [], []
#       def push(self, x):
#           self.stack.append(x)
#           self.mins.append(min(x, self.mins[-1]) if self.mins else x)
#       def pop(self):
#           self.stack.pop(); self.mins.pop()
#       def top(self): return self.stack[-1]
#       def getMin(self): return self.mins[-1]
# ===== End Interview Notes =====
