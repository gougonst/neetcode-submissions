# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        return self.mergeSort(lists, 0, len(lists) - 1)

    def mergeSort(self, lists: List[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        m = l + (r - l) // 2
        left = self.mergeSort(lists, l, m)
        right = self.mergeSort(lists, m + 1, r)
        return self.merge2Lists(left, right)

    def merge2Lists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if not left:
            return right
        if not right:
            return left
        
        mergedList = ListNode(0, None)
        cur = mergedList
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        cur.next = left or right
        return mergedList.next