# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        nodeToPathSum = {}

        def postorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            postorder(node.left)
            postorder(node.right)

            nonlocal maxSum, nodeToPathSum

            leftSum = nodeToPathSum.get(node.left, 0)
            rightSum = nodeToPathSum.get(node.right, 0)

            nodeToPathSum[node] = max(
                node.val, 
                node.val + leftSum, 
                node.val + rightSum
            )
            maxSum = max(
                maxSum, 
                nodeToPathSum[node], 
                node.val + leftSum + rightSum
            )

        postorder(root)
        return maxSum