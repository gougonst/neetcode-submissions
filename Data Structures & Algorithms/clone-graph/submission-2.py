"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copied = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            if node.val in copied:
                return copied[node.val]

            copy = Node(node.val)
            copied[node.val] = copy

            # For each child, do dfs to get the copied node
            copyNeighbors = []
            for neighbor in node.neighbors:
                copyNeighbor = dfs(neighbor)
                copyNeighbors.append(copyNeighbor)
            copy.neighbors = copyNeighbors
            return copy
        
        return dfs(node)