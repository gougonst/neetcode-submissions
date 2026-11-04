"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_mapping = {}
        dummy = Node(0, None, None)

        prev = dummy
        cur = head
        while cur:
            copy = Node(cur.val, None, None)
            node_mapping[cur] = copy
            prev.next = copy
            prev = copy
            cur = cur.next
        
        cur = head
        while cur:
            if cur.random is None:
                cur = cur.next
                continue
            copy = node_mapping[cur]
            copy.random = node_mapping[cur.random]
            cur = cur.next

        return dummy.next
        