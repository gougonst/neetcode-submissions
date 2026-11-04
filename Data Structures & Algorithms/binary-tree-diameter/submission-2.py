# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getDepth(root)
        return self.diameter

    def getDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        leftDepth = self.getDepth(node.left)
        rightDepth = self.getDepth(node.right)

        self.diameter = max(self.diameter, leftDepth + rightDepth)

        return 1 + max(leftDepth, rightDepth)
    