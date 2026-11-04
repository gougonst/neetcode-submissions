# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            successor, newRight = self.extractMin(root.right)
            successor.left = root.left
            successor.right = newRight
            return successor
        
        return root

    def extractMin(self, node: TreeNode) -> Tuple[TreeNode, Optional[TreeNode]]:
        if node.left is None:
            return node, node.right

        successor, subtree = self.extractMin(node.left)
        node.left = subtree
        return successor, node

