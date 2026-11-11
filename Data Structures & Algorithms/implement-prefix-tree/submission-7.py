class TrieNode:
    def __init__(self, c, children=None, word_ends=False):
        self.c = c
        self.children: dict[str] = children if children else {}
        self.word_ends = word_ends


class PrefixTree:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        while i < len(word):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                i += 1
            else:
                # Fill the rest of the word
                while i < len(word):
                    node = TrieNode(word[i])
                    curr.children[word[i]] = node
                    curr = node
                    i += 1
        curr.word_ends = True

    def search(self, word: str, end_sensitive: bool = True) -> bool:
        curr = self.root
        i = 0
        while i < len(word):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                i += 1
            else:
                return False
        return curr.word_ends if end_sensitive else True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, end_sensitive=False)
        