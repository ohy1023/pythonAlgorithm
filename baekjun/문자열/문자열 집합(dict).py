import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())

    res = 0

    str_dict = {}

    for _ in range(n):
        str_dict[input().strip()] = True

    for _ in range(m):
        data = input().strip()
        if data in str_dict.keys():
            res += 1

    print(res)
