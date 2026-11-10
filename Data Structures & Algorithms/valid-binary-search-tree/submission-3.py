# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True

        q = [(root, float("-inf"), float("inf"))]
        
        while q:
            node, mi, ma = q.pop(0)

            # Go through children
            if node.left:
                if node.left.val >= node.val or node.left.val >= ma or node.left.val <= mi: 
                    return False
                q.append((node.left, mi, node.val))
            if node.right:
                if node.right.val <= node.val or node.right.val >= ma or node.right.val <= mi:
                    return False
                q.append((node.right, node.val, ma))
            
        return True