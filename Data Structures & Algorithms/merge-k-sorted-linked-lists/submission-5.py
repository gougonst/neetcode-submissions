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

    def mergeSort(self, lists: List[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
        if l == r:
            return lists[l]
        m = l + (r - l) // 2
        left = self.mergeSort(lists, l, m)
        right = self.mergeSort(lists, m + 1, r)
        return self.merge2Lists(left, right)

    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return head.next