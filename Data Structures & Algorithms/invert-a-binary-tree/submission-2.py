# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Postorder traversal: Left, Right, Mid
        if not root:
            return None
        
        invertedLeft = self.invertTree(root.left)
        invertedRight = self.invertTree(root.right)
        root.left = invertedRight
        root.right = invertedLeft
        return root