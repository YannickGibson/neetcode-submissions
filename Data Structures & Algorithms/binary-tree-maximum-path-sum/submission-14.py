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
            if node is None: return float("-inf")
            res1 = dfs(node.left)
            res2 = dfs(node.right)
            
            # Select best path sum
            node.best, node.other = 0, 0
            if node.left and node.right:
                node.best = max(node.right.best, node.left.best)
                node.other = min(node.right.best, node.left.best)
            elif node.left:
                node.best = node.left.best
            elif node.right:
                node.best = node.right.best
            node.best = max(node.val + node.best, node.val)  # Possible end path
            return  max(res1, res2, node.best + max(0, node.other))

        return dfs(root)