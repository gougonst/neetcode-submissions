# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        nodeMaxSum = {} # Node: Max sum when node as root
        maxSum = float("-inf")

        def postorder(cur: Optional[TreeNode]) -> None:
            if not cur:
                return

            nonlocal nodeMaxSum, maxSum

            if cur in nodeMaxSum:
                return

            postorder(cur.left)
            postorder(cur.right)

            leftVal = nodeMaxSum.get(cur.left, 0)
            rightVal = nodeMaxSum.get(cur.right, 0)

            nodeMaxSum[cur] = max(
                cur.val, 
                cur.val + leftVal, 
                cur.val + rightVal, 
            )

            maxSum = max(
                maxSum, 
                nodeMaxSum[cur], 
                cur.val + leftVal + rightVal
            )

        postorder(root)
        return maxSum
