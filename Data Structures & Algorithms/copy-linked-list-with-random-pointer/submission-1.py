"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        our = dummy
        
        random_map = {}  # new: old random
        old_to_new = {}  # old: new

        # Copy with links
        curr = head
        while curr:
            our.next = Node(curr.val)
            random_map[our.next] = curr.random
            old_to_new[curr] = our.next
            our = our.next
            curr = curr.next

        # Copy randoms
        our = dummy.next
        while our:
            if random_map[our]:
                our.random = old_to_new[random_map[our]]
            our = our.next
        return dummy.next
            
            