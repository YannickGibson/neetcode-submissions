"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if not root: return None

        stack = [root]
        res = Node(root.val, neighbors=[])
        res_stack = [res]
        seen = {root: res}  # original: copy

        while stack:
            tail = stack.pop()
            res_tail = res_stack.pop()
            for node in tail.neighbors:
                if not node in seen:
                    stack.append(node)  # Continue DFS
                    created = Node(node.val, [])  # Create copy
                    res_stack.append(created)  # Continue cloned DFS
                    res_tail.neighbors.append(created)  # Link parent to neighbor
                    seen[node] = created  # Store orig: copy for future reverse link 
                else:  # Reverse link (node was already popped out of stack)
                    recovered = seen[node]
                    res_tail.neighbors.append(recovered)
        return res
