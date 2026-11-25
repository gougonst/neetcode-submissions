# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndices = { val: i for i, val in enumerate(inorder) }

        preIdx = 0

        def buildSubTree(l: int, r: int) -> Optional[TreeNode]:
            nonlocal preIdx
            if l > r:
                return None
            if preIdx >= len(preorder):
                return None
            
            val = preorder[preIdx]
            preIdx += 1
            inIdx = inorderIndices[val]
            node = TreeNode(val)
            node.left = buildSubTree(l, inIdx - 1)
            node.right = buildSubTree(inIdx + 1, r)
            return node

        return buildSubTree(0, len(preorder) - 1)