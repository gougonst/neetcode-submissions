# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], l: int, r: int) -> bool:
            if not node:
                return True

            if l >= node.val or r <= node.val:
                return False

            return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)

        return dfs(root, float("-inf"), float("inf"))