class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        res = float("-inf")
        stack = []
        node = root
        ret = 0

        while node is not None or stack:
            if node is not None:
                stack.append(node)
                stack.append(None)
                node = node.left
                ret = 0

            elif stack[-1] is None:
                stack[-1] = max(ret, 0)
                node = stack[-2].right
                ret = 0

            else:
                best1 = stack.pop()
                best2 = max(ret, 0)
                val = stack.pop().val

                res = max(res, best1 + best2 + val)
                ret = val + max(best1, best2)

        return res