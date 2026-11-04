# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root, 0)

    def getDepth(self, node: Optional[TreeNode], depth: int) -> int:
        if node is None:
            return depth
        
        return max(self.getDepth(node.left, depth + 1), 
                   self.getDepth(node.right, depth + 1))