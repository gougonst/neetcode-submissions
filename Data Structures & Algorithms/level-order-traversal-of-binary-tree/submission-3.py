# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        q = deque([root])
        while q:
            level = []
            qLen = len(q)
            for _ in range(qLen):
                node = q.pop()
                if node:
                    level.append(node.val)
                    q.appendleft(node.left)
                    q.appendleft(node.right)
            if level:
                levels.append(level)

        return levels