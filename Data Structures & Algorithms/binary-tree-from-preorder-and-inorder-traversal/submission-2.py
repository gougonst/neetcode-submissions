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

        head = TreeNode(preorder[0])

        preIdx = 1
        def buildSubTree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preIdx
            if preIdx >= len(preorder):
                return None
            inIdx = inorderIndices[preorder[preIdx]]
            if inIdx < left or inIdx > right:
                return None
            
            value = inorder[inIdx]
            node = TreeNode(value)
            preIdx += 1
            node.left = buildSubTree(left, inorderIndices[value] - 1)
            node.right = buildSubTree(inorderIndices[value] + 1, right)

            return node

        head.left = buildSubTree(0, inorderIndices[preorder[0]] - 1)
        head.right = buildSubTree(inorderIndices[preorder[0]] + 1, len(preorder) - 1)
        return head