# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x: int, y: int) -> int:
            if y == 0:
                return x
            return gcd(y, x % y)

        prev, cur = head, head.next
        while cur is not None:
            gcdNode = ListNode(gcd(prev.val, cur.val), None)
            prev.next = gcdNode
            gcdNode.next = cur
            prev = cur
            cur = cur.next

        return head