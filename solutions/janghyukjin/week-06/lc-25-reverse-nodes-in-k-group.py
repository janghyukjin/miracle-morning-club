from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """그룹별 반복 뒤집기 — dummy + 3포인터. O(n) / O(1)

    각 그룹마다 group_prev 에서 k칸 전진해 kth 를 찾고(모자라면 종료),
    prev 를 group_next 로 초기화한 상태로 뒤집어 꼬리를 자동 연결한다.
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 이번 그룹의 마지막 노드 찾기 — k개가 안 남으면 나머지는 그대로 둔다
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # 뒤집기 전에 다음 그룹 시작을 확보
            group_next = kth.next

            # prev 를 group_next 로 초기화하면 그룹 꼬리가 알아서 이어진다
            cur = group_prev.next
            prev = group_next
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # 뒤집기 전 첫 노드가 이제 tail — 덮어쓰기 전에 저장해야 잃지 않는다
            tmp = group_prev.next
            group_prev.next = prev  # prev == kth, 그룹의 새 head
            group_prev = tmp
