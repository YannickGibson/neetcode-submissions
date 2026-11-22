class Node:
    def __init__(self, neighbors=None, end=False):
        self.neighbors = neighbors if neighbors else {}  # {letter: node}
        self.end = end

class WordDictionary:

    def __init__(self):
        self.dummy = Node()  # Trie

    def addWord(self, word: str) -> None:
        root = self.dummy
        for c in word:
            if c not in root.neighbors:
                root.neighbors[c] = Node()
            root = root.neighbors[c]
        root.end = True

    def search(self, word: str, i: int = 0, root: Node = None) -> bool:  #O(26*26*23)
        if root is None: root = self.dummy

        # End of word reached
        if i >= len(word):
            if root.end:
                return True
            else:
                return False

        c = word[i]
        # Search every out of 26 paths
        res = False
        if c == ".":
            for nei_node in root.neighbors.values():
                if self.search(word, i + 1, nei_node):
                    return True
            return False

        # Check match
        if c in root.neighbors:  # Found
            return self.search(word, i + 1, root.neighbors[c])
        else:
            return False  # Does not continue
        
