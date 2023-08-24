import sys
from collections import defaultdict

if __name__ == "__main__":
    input = sys.stdin.readline
    hash_map = defaultdict(int)
    total_cnt = 0
    while True:
        tree = input().strip()
        if not tree:
            break
        else:
            total_cnt += 1
            hash_map[tree] += 1

    for tree, cnt in sorted(hash_map.items()):
        print("%s %.4f" % (tree, (cnt / total_cnt * 100)))
