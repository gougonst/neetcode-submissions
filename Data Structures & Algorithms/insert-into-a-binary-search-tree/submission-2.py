# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        
        if not root:
            return newNode
        
        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = newNode
                    return root
                node = node.left
            elif val > node.val:
                if not node.right:
                    node.right = newNode
                    return root
                node = node.right
            else:
                # It should not happened, log the errors and return root
                return root

        # It should not happend, log the errors

