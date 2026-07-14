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
