class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"]
        # 5#Hello5#World
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": j+= 1
            word_len = int(s[i:j])
            word_start = j + 1
            word_end = word_start + word_len
            res.append(s[word_start:word_end])
            i = word_end
        return res

