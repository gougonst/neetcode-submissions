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

        head = TreeNode(0, left=root)
        prev, node = head, root
        while node and node.val != key:
            prev = node
            if key > node.val:
                node = node.right
            else:
                node = node.left
        
        if node is None:
            return root

        def updateParant(parant: TreeNode, node: TreeNode, new: TreeNode) -> None:
            if parant.left == node:
                parant.left = new
            else:
                parant.right = new

        if node.left is None and node.right is None:
            updateParant(prev, node, None)
        elif node.left and node.right is None:
            updateParant(prev, node, node.left)
        else:
            parentNode = None
            successorNode = node.right
            while successorNode.left is not None:
                parentNode = successorNode
                successorNode = successorNode.left

            if parentNode:
                parentNode.left = successorNode.right
                successorNode.right = node.right
            
            successorNode.left = node.left
            updateParant(prev, node, successorNode)
        return head.left

"""
Search the node

if node is leaf: delete it

if node has left child, no right child: replace it with left child

if node has right child, no left child or 
if node has both left and right child: 
    1) find right child's left most node, it is used to concat left child
    1) concat left child to previous found concat node
    2) replace node with right child
"""