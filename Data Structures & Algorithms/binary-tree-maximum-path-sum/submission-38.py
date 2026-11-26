class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        res = float("-inf")
        stack = [(root, 0, 0)]
        ret = 0

        while stack:
            node, state, best1 = stack.pop()

            if node is None:
                ret = 0
            elif state == 0:
                # Process left child
                stack.append((node, 1, 0))
                stack.append((node.left, 0, 0))
            elif state == 1:
                # Process right child
                stack.append((node, 2, max(ret, 0)))
                stack.append((node.right, 0, 0))
            else:
                best2 = max(ret, 0)
                res = max(res, best1 + best2 + node.val)
                ret = node.val + max(best1, best2)

        return res