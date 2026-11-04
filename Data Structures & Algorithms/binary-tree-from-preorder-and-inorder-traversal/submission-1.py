# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, v in enumerate(inorder):
            indices[v] = i

        cur = 0
        def dfs(l: int, r: int) -> Optional[TreeNode]:
            nonlocal cur

            if l > r:
                return None

            root = TreeNode(preorder[cur])
            mid = indices[preorder[cur]]
            cur += 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(preorder) - 1)
