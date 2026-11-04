# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodeCount = 0

        def dfs(node: Optional[TreeNode], maxAncestor: int):
            if not node:
                return

            nonlocal nodeCount
            if node.val >= maxAncestor:
                nodeCount += 1
                maxAncestor = node.val
            
            dfs(node.left, maxAncestor)
            dfs(node.right, maxAncestor)
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return nodeCount + 1