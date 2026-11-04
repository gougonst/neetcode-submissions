# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def getHeight(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            nonlocal isBalanced

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            
            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False

            return 1 + max(leftHeight, rightHeight)
        
        getHeight(root)
        return isBalanced
        