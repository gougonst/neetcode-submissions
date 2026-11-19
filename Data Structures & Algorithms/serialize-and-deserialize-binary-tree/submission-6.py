# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encodedNodes = []

        def inorder(cur: Optional[TreeNode]) -> None:
            nonlocal encodedNodes

            if not cur:
                encodedNodes.append("N")
                return
            
            encodedNodes.append(str(cur.val))
            inorder(cur.left)
            inorder(cur.right)

        inorder(root)
        return ",".join(encodedNodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")

        i = 0
        def inorder() -> Optional[TreeNode]:
            nonlocal i

            if i >= len(nodes):
                return None

            val = nodes[i]
            i += 1
            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = inorder()
            node.right = inorder()
            return node
        
        return inorder()