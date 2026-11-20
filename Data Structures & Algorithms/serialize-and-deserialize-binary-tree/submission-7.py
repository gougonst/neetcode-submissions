# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encodedTree = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                encodedTree.append('N')
                return
            
            encodedTree.append(str(node.val))
            inorder(node.left)
            inorder(node.right)

        inorder(root)
        return ','.join(encodedTree)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')

        i = 0
        def inorder() -> Optional[TreeNode]:
            nonlocal i

            val = nodes[i]
            i += 1

            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = inorder()
            node.right = inorder()
            return node

        return inorder()
