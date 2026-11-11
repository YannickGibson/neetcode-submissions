"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        
        clone_map = {}  # orig: clone
        def dfs(root):  # return new copy of root
            if root in clone_map: return clone_map[root]

            clone = Node(root.val)
            clone_map[root] = clone
            for nei in root.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(root) if root else None
