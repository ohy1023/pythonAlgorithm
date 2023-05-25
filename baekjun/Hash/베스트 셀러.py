import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    hash_map = {}
    for _ in range(n):
        book = input().rstrip()
        if book not in hash_map:
            hash_map[book] = 1
        else:
            hash_map[book] += 1

    print(sorted(sorted(hash_map.items()), key=lambda x: x[1], reverse=True)[0][0])
