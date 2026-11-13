# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(nodes, (node.val, i, node))

        head = ListNode(0, None)
        cur = head

        while nodes:
            val, i, node = heapq.heappop(nodes)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(nodes, (node.next.val, i, node.next))

        return head.next
