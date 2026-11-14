from collections import deque, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_counts = {l: 0 for l in t}
        for l in t: t_counts[l] += 1
        our_counts = {l: 0 for l in t_counts.keys()}
        n_required = 0
        min_len = float("inf")
        min_index, max_index = None, None
        q = deque()
        # ABCAC
        # AB|CACBA
        for index, l in enumerate(s):
            if l not in t_counts: continue

            q.append((l, index))
            our_counts[l] += 1
            if our_counts[l] - 1 < t_counts[l]:
                n_required += 1

            if n_required == len(t):
                # Remove the first letter
                while n_required == len(t):
                    first_letter, first_index = q.popleft()
                    our_counts[first_letter] -= 1
                    if our_counts[first_letter] < t_counts[first_letter]:
                        # removal made a dip
                        n_required -= 1
                curr_len = index - first_index + 1
                if curr_len < min_len:
                    min_len = index - first_index + 1
                    min_index = first_index
                    max_index = index
        
        
        if min_index is not None:
            return s[min_index:max_index+1]
        return ""
