class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 

        # xyzz
        #    r
        # l

        # abba
        #    r
        # l
        # counts = {a: 3, b: 2}
        # res = 3

        res = 0
        l = 0
        counts = {}
        for r in range(len(s)):
            
            if s[r] in counts and counts[s[r]] >= l:
                l = counts[s[r]] + 1
            counts[s[r]] = r
            res = max(res, r - l + 1)
            
            r += 1
        return res
