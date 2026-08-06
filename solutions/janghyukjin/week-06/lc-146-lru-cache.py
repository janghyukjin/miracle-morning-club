class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict[key].prev.next = self.dict[key].next
        self.dict[key].next.prev = self.dict[key].prev
        self.dict[key].next = self.head.next
        self.dict[key].prev = self.head
        self.head.next.prev = self.dict[key]
        self.head.next = self.dict[key]
        return self.dict[key].val

    def put(self, key: int, value: int) -> None:
        lru = self.tail.prev
        if key not in self.dict:
            node = Node(key, value)
            self.dict[key] = node
            self.dict[key].next = self.head.next
            self.dict[key].prev = self.head
            self.head.next.prev = self.dict[key]
            self.head.next = self.dict[key]
        else:
            self.dict[key].val = value
            self.dict[key].prev.next = self.dict[key].next
            self.dict[key].next.prev = self.dict[key].prev
            self.dict[key].next = self.head.next
            self.dict[key].prev = self.head
            self.head.next.prev = self.dict[key]
            self.head.next = self.dict[key]
        if len(self.dict.keys()) > self.cap:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            del self.dict[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# ----- 리팩터링 버전 (동작 동일, 중복 제거) -----
# 위 코드는 "떼어내기 2줄 + 맨 앞에 붙이기 4줄"이 get / put-if / put-else
# 세 곳에 그대로 반복된다. 작성 중 이 6줄에서 링크 누락·순서 뒤집힘으로
# 네 번 막혔으므로, 헬퍼로 묶으면 한 곳만 맞추면 세 곳이 해결된다.
#
#     def _remove(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#     def _insert_front(self, node):
#         node.next = self.head.next
#         node.prev = self.head
#         node.next.prev = node          # ← 세 곳에서 빠뜨렸던 링크
#         self.head.next = node
#
#     def get(self, key):
#         if key not in self.dict:
#             return -1
#         node = self.dict[key]
#         self._remove(node)
#         self._insert_front(node)
#         return node.val
#
#     def put(self, key, value):
#         if key in self.dict:
#             node = self.dict[key]
#             node.val = value
#             self._remove(node)
#             self._insert_front(node)
#             return                     # 크기 안 늘어남 → capacity 체크 없음
#         node = Node(key, value)
#         self.dict[key] = node
#         self._insert_front(node)
#         if len(self.dict) > self.cap:
#             lru = self.tail.prev
#             self._remove(lru)
#             del self.dict[lru.key]
#
# 규칙: 덮어쓸 포인터를 참조하는 작업을 먼저 끝낸다.
#       head.next 를 새 노드로 바꾸기 전에 원래 첫 노드의 prev 를 세팅해야 한다.
#       (이 순서를 뒤집으면 노드가 자기 자신을 prev 로 가리킨다)
