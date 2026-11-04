# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getDepth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            nonlocal diameter

            leftDepth = getDepth(node.left)
            rightDepth = getDepth(node.right)
            
            diameter = max(diameter, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)
        
        getDepth(root)
        return diameter