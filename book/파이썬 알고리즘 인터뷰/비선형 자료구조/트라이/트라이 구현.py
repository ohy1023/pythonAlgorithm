class Node:
    def __init__(self):
        self.child_dict = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.child_dict:
                node.child_dict[char] = Node()
            node = node.child_dict[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.child_dict:
                return False
            node = node.child_dict[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.child_dict:
                return False
            node = node.child_dict[char]

        return True
