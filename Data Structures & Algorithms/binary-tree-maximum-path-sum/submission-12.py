# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        # Convert nodes to new DS
        def compare_children(node):
            if node is None: return 0
            compare_children(node.left)
            compare_children(node.right)
            
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

        compare_children(root)


        # Top down DFS
        res = float("-inf")
        def top_down(node) -> None:
            if not node: return
            nonlocal res
            candidate = max(node.other, 0) + node.best  # Zero means possible end path
            res = max(res, candidate)
            top_down(node.left)
            top_down(node.right)
        top_down(root)
        return res