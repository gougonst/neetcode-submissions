# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.spanOfTree = {}

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False
        if not self.isValidBST(root.right):
            return False

        self.traverseTree(root)
        if root.left and self.spanOfTree[root.left][1] >= root.val:
            return False
        if root.right and self.spanOfTree[root.right][0] <= root.val:
            return False
        return True

    def traverseTree(self, node: Optional[TreeNode]) -> None:
        if not node:
            return
        if node in self.spanOfTree:
            return

        self.traverseTree(node.left)
        self.traverseTree(node.right)
        minimums, maximums = [node.val], [node.val]
        if node.left:
            minimums.append(self.spanOfTree[node.left][0])
            maximums.append(self.spanOfTree[node.left][1])
        if node.right:
            minimums.append(self.spanOfTree[node.right][0])
            maximums.append(self.spanOfTree[node.right][1])
        self.spanOfTree[node] = (min(minimums), max(maximums))

