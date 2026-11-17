# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndices = {}
        for i, val in enumerate(inorder):
            inorderIndices[val] = i

        preIdx = 0
        def buildSubTree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            nonlocal preIdx
            inIdx = inorderIndices[preorder[preIdx]]
            value = inorder[inIdx]
            node = TreeNode(value)
            preIdx += 1
            node.left = buildSubTree(left, inIdx - 1)
            node.right = buildSubTree(inIdx + 1, right)

            return node

        return buildSubTree(0, len(preorder) - 1)