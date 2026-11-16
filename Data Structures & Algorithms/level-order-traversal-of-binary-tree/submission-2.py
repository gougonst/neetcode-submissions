# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        
        stack = deque([root])
        while stack:
            level = []
            stackLen = len(stack)
            for _ in range(stackLen):
                node = stack.pop()
                level.append(node.val)
                if node.left:
                    stack.appendleft(node.left)
                if node.right:
                    stack.appendleft(node.right)
            levels.append(level)

        return levels