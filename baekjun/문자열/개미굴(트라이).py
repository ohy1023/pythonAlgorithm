import sys


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, foods):
        node = self.root
        for food in foods:
            if food not in node.children:
                node.children[food] = Node()
            node = node.children[food]
        node.is_end = True

    def dfs(self, current_node, depth):
        for k, v in sorted(current_node.children.items()):
            # 출력
            for _ in range(depth):
                print("--", end="")
            print(k)

            # 재귀
            self.dfs(v, depth + 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    trie = Trie()
    for i in range(n):
        data = list(input().split())
        trie.insert(data[1:])

    trie.dfs(trie.root, 0)
