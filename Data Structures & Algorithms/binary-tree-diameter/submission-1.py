# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        diameter = self.getDepth(root.left) + self.getDepth(root.right)
        return max(diameter, 
                   self.diameterOfBinaryTree(root.left), 
                   self.diameterOfBinaryTree(root.right))

    def getDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))