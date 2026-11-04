# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        