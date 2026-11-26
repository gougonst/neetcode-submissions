"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set([node.val])
        root = Node(node.val)

        newNodeMap = {root.val: root}

        q = deque([node])
        while q:
            qLen = len(q)
            for _ in range(qLen):
                n = q.popleft()
                newNode = newNodeMap[n.val]
                for neighbor in n.neighbors:
                    if neighbor.val not in newNodeMap:
                        newNodeMap[neighbor.val] = Node(neighbor.val)
                    newNeighbor = newNodeMap[neighbor.val]
                    newNode.neighbors.append(newNeighbor)
                    if neighbor.val in visited:
                        continue
                    visited.add(neighbor.val)
                    q.append(neighbor)

        return root
                    
                    

