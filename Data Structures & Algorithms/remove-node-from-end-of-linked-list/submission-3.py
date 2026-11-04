# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse the linked list
        head = Solution._reverse_linked_list(head)

        # Remove the nth node from reversed linked list
        head = Solution._remove_nth_node(head, n)

        # Reverse the linked list again
        head = Solution._reverse_linked_list(head)

        return head

    @staticmethod
    def _reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    @staticmethod
    def _remove_nth_node(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            return head.next

        prev, cur = None, head
        for i in range(n - 1):
            print(cur.val)
            prev = cur
            cur = cur.next
        # Handle deletion of the last node
        prev.next = cur.next if cur.next else None

        return head
