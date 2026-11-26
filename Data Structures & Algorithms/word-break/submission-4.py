class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:

        # i = 0
        # stack [8]
        # explored = {0, 5, 8, 13}

        i = 0
        stack = [i]
        explored = [False] * len(s)
        while stack:
            i = stack.pop()
            
            # Choose word
            for word in words:
                end = i + len(word)
                if end < len(s) and s[i:end] == word:
                    if explored[end]:
                        continue
                    stack.append(end)
                    explored[end] = True
                elif end == len(s) and s[i:end] == word:
                    return True
        return False