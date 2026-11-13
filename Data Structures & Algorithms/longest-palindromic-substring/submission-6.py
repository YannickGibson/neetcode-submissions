class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        streak = 0
        for i in range(len(s)):
            for offset in range(2):
                l, r = i, i + offset
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > streak:
                        streak = (r - l + 1)
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
        return res