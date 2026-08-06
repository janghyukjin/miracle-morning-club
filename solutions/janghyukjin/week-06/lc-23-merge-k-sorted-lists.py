import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """본인 풀이 — 매 스텝 k개 head 를 스캔해 최솟값 선택. O(N*k) / O(k)"""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0, None)
        now = head

        # cleansing
        tmp = []
        for v in lists:
            if v:
                tmp.append(v)

        lists = tmp

        while len(lists) > 0:
            candidates = []
            for v in lists:
                candidates.append(v.val)

            if len(candidates) == 0:
                break

            min_value = min(candidates)
            min_index = candidates.index(min_value)

            min_node = lists[min_index]
            if min_node.next is None:
                lists = lists[:min_index] + lists[min_index + 1:]
            else:
                lists[min_index] = min_node.next

            now.next = min_node
            now = now.next
            now.next = None

        return head.next


class SolutionHeap:
    """최적화 — 최솟값 선택을 min-heap 으로. O(N log k) / O(k)"""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # 각 리스트의 head 만 넣는다 → 힙 크기는 항상 k 이하
        for i, node in enumerate(lists):
            if node:                                # 빈 리스트(None) 제외
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        cur = dummy

        while heap:
            _, i, node = heapq.heappop(heap)        # 최솟값
            cur.next = node
            cur = cur.next
            if node.next:                           # 같은 리스트의 다음 후보를 채운다
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# 두 풀이 차이 (실측, 각 리스트 100노드)
#
#   k=  50  N=  5,000    min(): 10.1 ms    heap:  2.1 ms   ->  4.9배
#   k= 200  N= 20,000    min(): 133.5 ms   heap: 11.1 ms   -> 12.0배
#   k= 500  N= 50,000    min(): 829.6 ms   heap: 30.0 ms   -> 27.7배
#   k=1000  N=100,000    min(): 3313.7 ms  heap: 80.6 ms   -> 41.1배
#
# k 가 커질수록 배율도 커진다 = 상수 차이가 아니라 복잡도 차이.
# 본인 풀이는 반복 1회당 O(k) 스캔이 네 번이다:
#   ① candidates 재구성  ② min()  ③ .index()  ④ 슬라이싱 재할당
# heap 은 이걸 heappop + heappush = O(log k) 로 압축한다.
# 실제로 바뀌는 건 리스트 하나의 head 뿐인데 매번 k개를 다시 읽는 것이 낭비.
#
# heap 튜플에 i(리스트 번호)를 끼우는 이유: 값이 같을 때 heapq 가 세 번째 칸의
# ListNode 를 비교하려 해서 TypeError. i 는 힙에 리스트당 항목이 하나뿐이라는
# 불변식 덕에 항상 유일하므로 비교가 두 번째 칸에서 끝난다.
#
# 면접 서술: brute force(매번 k개 스캔) -> "최솟값만 싸게 얻으면 된다" -> heap.
# 각 리스트가 이미 정렬돼 있으므로 후보는 head k개로 충분하다는 것이 핵심.
# 전체를 sorted() 로 다시 정렬하는 풀이는 이 전제를 버리는 것이라 감점.


# ===== Interview Notes =====
# [Merge k Sorted Lists] Hard · Heap / Divide and Conquer
#
# [접근법]
#   1. Min heap — O(n log k) / O(k)
#      (val, idx, node) 튜플로 비교
#   2. Divide and conquer — O(n log k) / O(log k)
#      두 리스트씩 병합 반복
#
# [Follow-up 질문 (면접 단골)]
#   - 외부 정렬 (external sort)?
#   - lists가 매우 크면? (스트리밍)
#   - weighted merge?
#
# [Pitfalls / 흔한 실수]
#   - heapq는 첫 원소가 같으면 다음 원소 비교 — ListNode는 비교 불가 → idx tiebreak
#   - 빈 리스트 / lists=[]
#
# [최적해 (참고)]
#   import heapq
#   h = []
#   for i, l in enumerate(lists):
#       if l: heapq.heappush(h, (l.val, i, l))
#   dummy = cur = ListNode()
#   while h:
#       val, i, node = heapq.heappop(h)
#       cur.next = node; cur = node
#       if node.next: heapq.heappush(h, (node.next.val, i, node.next))
#   return dummy.next
# ===== End Interview Notes =====
