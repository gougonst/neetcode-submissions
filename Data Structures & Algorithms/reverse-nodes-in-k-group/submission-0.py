# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = head, head
        prev = dummy

        # Walk through the list and reverse partition every K steps.
        while fast is not None:
            counter = 0
            while counter < k and fast is not None:
                fast = fast.next
                counter += 1

            # If counter < k, it means the partition is fewer than K nodes.
            if counter < k:
                break
            
            # Reverse the partition
            reversePart = self.reversePartition(slow, k)
            prev.next = reversePart

            while prev.next is not None:
                prev = prev.next
            prev.next = fast

            slow = fast

        return dummy.next

    def reversePartition(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, prev = head, None
        for _ in range(k):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

        