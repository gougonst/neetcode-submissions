# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counter = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        val = self.kthSmallest(root.left, k)
        if val != -1:
            return val
        self.counter += 1
        if self.counter == k:
            return root.val
        val = self.kthSmallest(root.right, k)
        if val != -1:
            return val
        return -1