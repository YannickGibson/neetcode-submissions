# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest):
            if not node:
                return 0

            left = dfs(node.left, max(largest, node.val))
            right = dfs(node.right, max(largest, node.val))
            bonus = 1 if node.val >= largest else 0
            return left + right + bonus

        return dfs(root, largest=float("-inf"))