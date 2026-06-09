class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            current_min = min(value, self.stack[-1][1])
            self.stack.append((value, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# ===== Interview Notes =====
# [Min Stack] Medium · Stack Design
#
# [접근법]
#   1. Pair Stack (value, running_min) — O(1) / O(n)
#      본인 풀이: 각 원소를 (값, 그 시점까지의 최소) 튜플로 저장.
#      push 시 직전 top의 min과 비교해 둘 중 작은 값을 새 min으로 기록.
#   2. Two Stacks (값 스택 + 최소 스택) — O(1) / O(n)
#      별도의 min 스택을 유지. push 시 min_stack[-1] 보다 작거나 같을 때만 푸시.
#   3. Encoded Single Stack (공간 최적) — O(1) / O(n) but 상수 절약
#      현재 min과의 차이를 저장하는 트릭. 면접에선 잘 안 묻고 가독성↓.
#
# [핵심 아이디어]
#   - getMin이 O(1)이려면 "스택의 각 시점에서의 최솟값"을 함께 기억해야 한다.
#   - 새로 들어오는 값이 작아질 수도/그대로일 수도 있으므로
#     "직전 min과 새 value 중 작은 값" 을 항상 함께 저장.
#
# [Follow-up 질문 (면접 단골)]
#   - 공간을 더 줄일 수 있나? → Two stack 변형(중복된 min 안 푸시) 또는 인코딩 트릭.
#   - getMax도 추가하려면? → 동일 패턴으로 (val, min, max) 트리플.
#   - thread-safe 하게 만들려면? → 락 또는 immutable 구조.
#   - 중간 인덱스 접근/삭제도 필요하면? → 이건 더 이상 stack 문제 아님 (heap+lazy delete).
#
# [Pitfalls / 흔한 실수]
#   - getMin 호출 시 stack 전체를 O(n)으로 훑으면 요구사항 위반(모든 op O(1)).
#   - 첫 push에서 self.stack[-1] 접근하면 IndexError → empty 분기 필수.
#   - pop 후 min을 재계산하려 하면 O(n). 튜플로 함께 저장하면 자동으로 해결.
#   - Two stack 방식에서 동률 처리(<=)를 빠뜨리면 같은 min이 일찍 사라짐.
#
# [복잡도]
#   - Time: push/pop/top/getMin 모두 O(1)
#   - Space: O(n)
#
# [최적해 (참고) — Two stacks, 중복 min 제거]
#   class MinStack:
#       def __init__(self):
#           self.s, self.m = [], []
#       def push(self, x):
#           self.s.append(x)
#           if not self.m or x <= self.m[-1]:
#               self.m.append(x)
#       def pop(self):
#           if self.s.pop() == self.m[-1]:
#               self.m.pop()
#       def top(self): return self.s[-1]
#       def getMin(self): return self.m[-1]
# ===== End Interview Notes =====
