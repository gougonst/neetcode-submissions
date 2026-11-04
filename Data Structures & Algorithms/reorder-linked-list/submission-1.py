# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # Use slow and fast pointer to find the median node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide the linked list to left and right partition
        left = head
        right = slow.next
        slow.next = None

        # Reverse the right partition
        prev, cur = None, right
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        right = prev

        # Concatenate the left and reversed right partition one by one
        cur_l, cur_r = left, right
        while cur_r:
            next_l, next_r = cur_l.next, cur_r.next
            cur_l.next = cur_r
            cur_r.next = next_l
            cur_l, cur_r = next_l, next_r
        