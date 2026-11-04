# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Add them start with low digit
        dummy = ListNode()
        prev = dummy
        is_carry = 0
        while l1 or l2:
            l1 = ListNode() if not l1 else l1
            l2 = ListNode() if not l2 else l2
            sum = l1.val + l2.val + is_carry
            cur = ListNode(sum % 10)
            prev.next = cur
            prev = cur
            l1, l2 = l1.next, l2.next
            is_carry = sum // 10

        if is_carry:
            prev.next = ListNode(1)

        return dummy.next

    @staticmethod
    def _reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
