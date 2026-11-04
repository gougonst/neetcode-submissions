# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)

    def mergeSort(self, lists: List[Optional[ListNode]], l: int, r: int) -> ListNode:
        if l > r:
            return None
        if l == r:
            return lists[l]

        m = l + (r - l) // 2
        left = self.mergeSort(lists, l, m)
        right = self.mergeSort(lists, m + 1, r)
        return self.merge2Lists(left, right)

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
