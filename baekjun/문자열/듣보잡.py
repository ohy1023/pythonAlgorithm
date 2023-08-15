import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())

    list_n = set(input().strip() for _ in range(n))
    list_m = set(input().strip() for _ in range(m))

    result = list(list_n & list_m)

    result.sort()

    print(len(result), *result, sep="\n")
