# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(a: Optional[TreeNode], b: Optional[TreeNode]):
            # Leaf node check
            if not a and not b: return True
            if not a and b or a and not b: return False

            # Value Check
            if a.val != b.val: return False

            # Recursion
            return isSame(a.left, b.left) and isSame(a.right, b.right)

        same = isSame(root, subRoot)
        if root:
            return same or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return same


        