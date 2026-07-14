from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        cur = tmp
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            add = x + y + carry
            val = add % 10
            carry = add // 10
            cur.next = ListNode(val)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return tmp.next


# ===== Interview Notes =====
# [Add Two Numbers] Medium · Linked List Math (carry)
#
# [접근법]
#   1. Simulate with carry — O(max(m,n)) / O(max(m,n))
#
# [Follow-up 질문 (면접 단골)]
#   - LC 445 (정상 자릿수 순서, 즉 큰 자리부터)? → stack 또는 reverse
#   - subtract version?
#   - 10진수 아닌 기수?
#
# [Pitfalls / 흔한 실수]
#   - carry가 마지막에 남으면 새 노드 추가
#   - 한 쪽이 더 길 때
#   - dummy head 사용 권장
#
# [최적해 (참고)]
#   dummy = ListNode()
#   cur, carry = dummy, 0
#   while l1 or l2 or carry:
#       s = carry
#       if l1: s += l1.val; l1 = l1.next
#       if l2: s += l2.val; l2 = l2.next
#       carry, val = divmod(s, 10)
#       cur.next = ListNode(val)
#       cur = cur.next
#   return dummy.next
# ===== End Interview Notes =====
