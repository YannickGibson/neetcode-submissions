# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        res = float("-inf")
        # Convert nodes to new DS
        def dfs(node):
            if node is None: return 0
            best1 = dfs(node.left)
            best2 = dfs(node.right)
            # Select best path sum from children
            best = max(0, best1) + max(0, best2) + node.val  # Possible end path
            nonlocal res
            res = max(res, best)
            return node.val + max(best1, best2, 0)
        dfs(root)
        return res