# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.best = 0  # best subtree sum + val
        self.other = 0  # worse subtree sum
        self.parent = parent

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        # Convert nodes to new DS
        nodes = defaultdict(list)
        max_level = -1
        def convert_nodes(node, parent=None, level=0):
            nonlocal max_level
            if node is None: return None
            res = Node(val=node.val, parent=parent)
            res.left = convert_nodes(node.left, res, level + 1)
            res.right = convert_nodes(node.right, res, level + 1)
            if max_level < level: 
                max_level = level
            nodes[level].append(res)
            return res
        root = convert_nodes(root)

        # First bottom up approach
        for level in reversed(range(max_level + 1)):
            for node in nodes[level]:
                if node.left and node.right:
                    node.best = max(node.right.best, node.left.best)
                    node.other = min(node.right.best, node.left.best)
                elif node.left:
                    node.best = node.left.best
                elif node.right:
                    node.best = node.right.best
                node.best = max(node.val + node.best, node.val)  # Possible end path

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