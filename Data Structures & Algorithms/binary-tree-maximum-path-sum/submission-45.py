# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = root.val

        def dfs(node):
            if not node: return 0
            left_best = max(0, dfs(node.left))
            right_best = max(0, dfs(node.right))

            candidate = node.val + left_best + right_best

            nonlocal max_sum
            max_sum = max(max_sum, candidate)

            return node.val + max(left_best, right_best)


        dfs(root)

        return max_sum