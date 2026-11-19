# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encodedTree = ""

        def preorder(node: Optional[TreeNode]) -> None:
            nonlocal encodedTree

            if not node:
                encodedTree += "#,"
                return
            
            encodedTree += str(node.val) + ","
            
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return encodedTree

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def buildNode(i: int) -> (int, Optional[TreeNode]):
            if data[i] == ",":
                i += 1

            if data[i] == "#":
                return i + 1, None
            
            val = ""
            while data[i] != "," and data[i] != "#":
                val += data[i]
                i += 1
            return i, TreeNode(int(val))

        def buildTree() -> Optional[TreeNode]:
            nonlocal cur

            cur, node = buildNode(cur)
            if not node:
                return None

            node.left = buildTree()
            node.right = buildTree()
            return node

        cur = 0
        return buildTree()



