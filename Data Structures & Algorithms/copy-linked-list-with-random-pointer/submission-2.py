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
        node_mapping = collections.defaultdict(lambda: Node(0))
        node_mapping[None] = None
        
        cur = head
        while cur:
            node_mapping[cur].val = cur.val
            node_mapping[cur].next = node_mapping[cur.next]
            node_mapping[cur].random = node_mapping[cur.random]
            cur = cur.next

        return node_mapping[head]