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
        node_mapping = {None: None}
        
        cur = head
        while cur:
            if cur not in node_mapping:
                node_mapping[cur] = Node(0)
            node_mapping[cur].val = cur.val

            if cur.next:
                if cur.next not in node_mapping:
                    node_mapping[cur.next] = Node(0)
                node_mapping[cur].next = node_mapping[cur.next]

            if cur.random:
                if cur.random not in node_mapping:
                    node_mapping[cur.random] = Node(0)
                node_mapping[cur].random = node_mapping[cur.random]
            
            cur = cur.next
        
        copied_head = node_mapping[head]

        return node_mapping[head]