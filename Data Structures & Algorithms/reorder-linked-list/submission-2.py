# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        half, last = head, head
        while last.next and last.next.next:
            half = half.next
            last = last.next.next

        prev, cur = None, half.next
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        half.next = None

        l1, l2 = head, prev
        while l2:
            l1next = l1.next
            l2next = l2.next
            l1.next = l2
            l2.next = l1next
            l1 = l1next
            l2 = l2next


