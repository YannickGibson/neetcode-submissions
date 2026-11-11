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
        stack, res_stack = [root], [Node(root.val, neighbors=[])]
        seen = {root: res_stack[0]}  # original: copy
        while stack:
            tail = res_stack.pop()
            for node in stack.pop().neighbors:
                if not node in seen:
                    stack.append(node)  # Continue DFS
                    created = Node(node.val, [])  # Create copy
                    res_stack.append(created)  # Continue cloned DFS
                    tail.neighbors.append(created)  # Link parent to neighbor
                    seen[node] = created  # Store orig: copy for future reverse link 
                else:  # Reverse link (node was already popped out of stack)
                    tail.neighbors.append(seen[node])
        return seen[root]
