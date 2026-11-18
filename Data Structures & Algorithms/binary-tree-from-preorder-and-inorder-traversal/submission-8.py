# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inIndices = { val: i for i, val in enumerate(inorder) }

        pIdx = 0
        def buildSubTree(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            
            nonlocal pIdx
            val = preorder[pIdx]
            iIdx = inIndices[val]

            pIdx += 1
            node = TreeNode(val)
            node.left = buildSubTree(l, iIdx - 1)
            node.right = buildSubTree(iIdx + 1, r)
            return node

        return buildSubTree(0, len(inorder) - 1)