# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        l, r = head, prev
        while r:
            lnext, rnext = l.next, r.next
            l.next = r
            r.next = lnext
            l = lnext
            r = rnext