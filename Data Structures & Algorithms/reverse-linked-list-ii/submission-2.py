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

        i = 1
        while i != left:
            prev = cur
            cur = cur.next
            i += 1

        prevNode = prev
        leftNode = cur

        # Reverse
        while i != right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            i += 1

        leftNode.next = cur.next
        prevNode.next = cur
        cur.next = prev
        
        return root.next