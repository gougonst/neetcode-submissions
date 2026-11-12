# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        first, second = head, head.next
        while first != second:
            if (
                not first.next 
                or not second.next 
                or not second.next.next
            ):
                return False

            first = first.next
            second = second.next.next

        return True