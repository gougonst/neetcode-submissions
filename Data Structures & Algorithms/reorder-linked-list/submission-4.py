# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the last element of first half
        # Slow will be the last element of first half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # Concatenate two halves
        l1, l2 = head, prev
        while l2:
            l1next, l2next = l1.next, l2.next
            l1.next = l2
            l2.next = l1next
            l1 = l1next
            l2 = l2next