class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minstack) == 0:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value,self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]



# ===== Interview Notes =====
# [Min Stack] Medium · Stack Design
# URL: https://leetcode.com/problems/min-stack/
#
# [힌트]
#   - 모든 연산은 O(1)이어야 한다.
#   - 값 stack과 현재 minimum을 추적하는 보조 stack을 분리해봐.
#   - 같은 minimum 값이 여러 번 들어오는 경우를 조심.
#
# [체크]
#   - push: 새 값이 현재 min 이하일 때 min stack도 업데이트?
#   - pop: pop되는 값이 현재 min이면 min stack도 같이 pop?
#   - top/getMin: 비어 있는 stack 호출은 LeetCode 제약상 없다고 봐도 됨.
# ===== End Interview Notes =====
