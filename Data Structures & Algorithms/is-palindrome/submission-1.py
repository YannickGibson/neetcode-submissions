class Solution:
    def isPalindrome(self, s: str) -> bool:
        reduced = ""
        s = s.lower()
        for character in s:
            c = ord(character)
            if c >= ord("a") and c <= ord("z") or \
               c >= ord("0") and c <= ord("9"):
                reduced += character
        return reduced == "".join(reversed(reduced))
