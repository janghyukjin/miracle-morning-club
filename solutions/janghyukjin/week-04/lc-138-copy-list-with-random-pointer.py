from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}
        cur = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mp[cur].next = mp[cur.next] if cur.next else None
            mp[cur].random = mp[cur.random] if cur.random else None
            cur = cur.next

        return mp[head]


# ===== Interview Notes =====
# [Copy List with Random Pointer] Medium · Hash Map / Interleaving
#
# [접근법]
#   1. Hash map (old → new) — O(n) / O(n)
#      두 번 순회
#   2. Interleave (최적 공간) — O(n) / O(1)
#      원본-복사 교대 후 분리
#
# [Follow-up 질문 (면접 단골)]
#   - 일반 그래프 deep copy (LC 133)?
#   - thread-safe하게?
#   - iterative vs recursive
#
# [Pitfalls / 흔한 실수]
#   - random=None 처리
#   - interleave 분리 시 원본도 복원해야 (보통)
#
# [최적해 (참고)]
#   if not head: return None
#   old_to_new = {}
#   cur = head
#   while cur:
#       old_to_new[cur] = Node(cur.val)
#       cur = cur.next
#   cur = head
#   while cur:
#       old_to_new[cur].next = old_to_new.get(cur.next)
#       old_to_new[cur].random = old_to_new.get(cur.random)
#       cur = cur.next
#   return old_to_new[head]
# ===== End Interview Notes =====
