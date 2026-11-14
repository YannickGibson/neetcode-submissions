from collections import deque, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        class Node: 
            def __init__(self, index, prev=None, next=None):
                self.index = index
                self.prev = prev
                self.next = next
        # 1. add biggest index at end
        # -> unlink last node
        # 2. get smallest index value 
        # -> unlink first node
        # 3. remove arbitrary value index and preserve order


        # s = "ijxk?i"
        # t = kxji
        # node_map {i->Node(5): j: Node(1), x: Node(2), k: Node(3)}
        # dummy <-> Node(1) <-> Node(2) <-> Node(3) <- Node(5) 
        #                                               tail

        # b = Node(0)
        # a = dummy, b = Node(1)
        # f = 1
        # l = 5   => 5 as min len

        dummy = Node(index=None)
        tail = dummy
        node_map = defaultdict(deque)
        all_count = 0
        our_counts = defaultdict(int)
        t_counts = {letter: 0 for letter in set(t)}
        for c in t: 
            t_counts[c] += 1
        
        min_len = len(s) + 1
        min_f, min_l = None, None
        for i, letter in enumerate(s):  # O(n * inner())
            if not letter in t_counts:
                continue

            # Remove node
            if len(node_map[letter]) == t_counts[letter]:
                # If tail, update tail
                b = node_map[letter].popleft()
                if b == tail:  # set new tail if tail is to be removed
                    tail = tail.prev
                # Unlink node
                a, c = b.prev, b.next 
                a.next = c
                if c: c.prev = a
            else:
                all_count += 1

            # Link new node
            tail.next = Node(i, prev=tail)
            node_map[letter].append(tail.next)
            tail = tail.next

            # Update min subsequence
            if all_count == len(t):
                first_index = dummy.next.index
                last_index = tail.index
                if last_index - first_index + 1 < min_len:
                    min_len = last_index - first_index + 1
                    min_f = first_index
                    min_l = last_index

        # Finally extract the subsequence
        if min_f is not None:
            return s[min_f:min_l+1]
        return ""
        