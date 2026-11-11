class TrieNode:
    def __init__(self):
        self.children: dict[str] = {}
        self.word_ends = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        curr.word_ends = True

    def search(self, word: str, end_sensitive: bool = True) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]

        return curr.word_ends if end_sensitive else True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, end_sensitive=False)
        