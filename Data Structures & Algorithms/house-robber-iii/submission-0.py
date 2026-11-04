# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo: Dict[Set(TreeNode, bool), int] = {}

        def dfs(node: Optional[TreeNode], canRob: bool) -> int:
            if node is None:
                return 0
            if (node, canRob) in memo:
                return memo[(node, canRob)]

            curValue = node.val if canRob else 0
            
            notRobLeft = dfs(node.left, False)
            notRobRight = dfs(node.right, False)
            robLeft = dfs(node.left, True)
            robRight = dfs(node.right, True)

            if canRob:
                curValue += notRobLeft
                curValue += notRobRight
            else:
                curValue += max(notRobLeft, robLeft)
                curValue += max(notRobRight, robRight)
            memo[(node, canRob)] = curValue
            return curValue

        return max(dfs(root, True), dfs(root, False))
