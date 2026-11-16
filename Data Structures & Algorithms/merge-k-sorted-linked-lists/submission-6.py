# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode(0, None)

        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        cur = ans
        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
            cur.next = node
            cur = cur.next

        return ans.next
