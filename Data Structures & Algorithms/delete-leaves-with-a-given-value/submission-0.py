# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postOrderDelete(node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            if node is None:
                return None

            node.left = postOrderDelete(node.left, target)
            node.right = postOrderDelete(node.right, target)

            # Is leave?
            if node.left is None and node.right is None:
                # Is match target?
                if node.val == target:
                    return None
            return node

        root = postOrderDelete(root, target)
        return root