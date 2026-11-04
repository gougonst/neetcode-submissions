# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], maxAncestor: int) -> int:
            if not node:
                return 0

            res = 0
            if node.val >= maxAncestor:
                maxAncestor = node.val
                res = 1
            res += dfs(node.left, maxAncestor)
            res += dfs(node.right, maxAncestor)
            return res

        return dfs(root, root.val)