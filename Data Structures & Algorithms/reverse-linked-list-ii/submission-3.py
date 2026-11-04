# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        leftNode, prevNode = None, None

        root = ListNode()
        root.next = head

        cur, prev = head, root

        for _ in range(1, left):
            prev = cur
            cur = cur.next

        prevNode = prev
        leftNode = cur

        # Reverse
        for _ in range(left, right):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        leftNode.next = cur.next
        prevNode.next = cur
        cur.next = prev
        
        return root.next