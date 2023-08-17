import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())

    str_set = set(input().strip() for _ in range(n))

    res = 0

    for _ in range(m):
        data = input().strip()
        if data in str_set:
            res += 1

    print(res)
