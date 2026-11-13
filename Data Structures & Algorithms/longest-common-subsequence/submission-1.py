from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        d = defaultdict(lambda: -1)  # till now, how much are we worth

        # banana
        #    i
        # anna
        #   j
        # match = 2

        # banana
        # i
        # anna
        #  j
        #


        def dfs(i, j, match):
            if i >= len(text1) or j >= len(text2):
                return match

            if d[(i, j)] < match:
                d[(i, j)] = match
            else:
                return -1

            # Match
            if text1[i] == text2[j]:
                return dfs(i + 1, j + 1, match + 1) 
            return max(dfs(i + 1, j, match), dfs(i, j + 1, match))

        return dfs(0, 0, 0)
