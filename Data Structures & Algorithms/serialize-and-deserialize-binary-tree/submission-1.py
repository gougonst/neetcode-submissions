# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        serializeTree = str(root.val)
        if not root.left and root.right:
            serializeTree += "#"
        elif not root.right and root.left:
            serializeTree += "@"
        elif root.left and root.right:
            serializeTree += "$"
        else:
            serializeTree += "!"
        return serializeTree + self.serialize(root.left) + self.serialize(root.right)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0

        def dfs(curData: str) -> Optional[TreeNode]:
            nonlocal i

            if i >= len(curData):
                return None

            curVal = ""
            while curData[i].isdigit():
                curVal += curData[i]
                i += 1
            curVal = int(curVal)
            curChild = curData[i]

            i += 1

            curNode = TreeNode(curVal)
            if curChild == "!":
                return curNode
            if curChild != "#":
                curNode.left = dfs(curData)
            if curChild != "@":
                curNode.right = dfs(curData)

            return curNode

        return dfs(data)
