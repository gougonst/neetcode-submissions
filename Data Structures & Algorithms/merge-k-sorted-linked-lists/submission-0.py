# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        if k == 2:
            return self.merge2Lists(lists[0], lists[1])

        
        mergedList = self.merge2Lists(
            self.mergeKLists(lists[:k // 2]), 
            self.mergeKLists(lists[k // 2:])
        )
        return mergedList

    def merge2Lists(self, left: Optional[ListNode], right: Optional[ListNode]) -> ListNode:
        if left is None:
            return right
        if right is None:
            return left

        dummy = ListNode()
        cur = dummy
        curLeft, curRight = left, right
        while curLeft and curRight:
            if curLeft.val > curRight.val:
                cur.next = curRight
                curRight = curRight.next
            else:
                cur.next = curLeft
                curLeft = curLeft.next
            cur = cur.next
        if curLeft:
            cur.next = curLeft
        elif curRight:
            cur.next = curRight
        return dummy.next
