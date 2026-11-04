# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf

        def postorder(node: Optional[TreeNode]) -> int:
            nonlocal res

            if not node:
                return 0

            lval = postorder(node.left)
            rval = postorder(node.right)

            lval = 0 if lval < 0 else lval
            rval = 0 if rval < 0 else rval
            
            res = max(res, 
                      lval + rval + node.val, 
                      lval + node.val, 
                      rval + node.val)
            return max(lval + node.val, rval + node.val)

        postorder(root)
        return res
        