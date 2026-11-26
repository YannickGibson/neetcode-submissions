# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        res = [root.val]
        # Convert nodes to new DS
        def dfs(node):
            if node is None: return 0
            best1 = max(dfs(node.left), 0)
            best2 = max(dfs(node.right), 0)
            # Select best path sum from children
            best = best1 + best2 + node.val  # Choose both
            res[0] = max(res[0], best)
            return node.val + max(best1, best2)  # Choose only one kid
        dfs(root)
        return res[0]