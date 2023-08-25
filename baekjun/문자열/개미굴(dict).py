import sys
from collections import defaultdict


def draw_ant_colony(info):
    ant_colony = defaultdict(list)

    for line in info:
        tokens = line.split()
        current_level = ant_colony

        for token in tokens:
            if token not in current_level:
                current_level[token] = defaultdict(list)
            current_level = current_level[token]

    def dfs(node, depth):
        for key, value in sorted(node.items()):
            print("--" * depth + key)
            dfs(value, depth + 1)

    dfs(ant_colony, 0)


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = [input().strip()[2:] for _ in range(n)]

    draw_ant_colony(arr)
