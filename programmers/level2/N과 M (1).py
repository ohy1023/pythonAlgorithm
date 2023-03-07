import sys


def DFS(v):
    if v == m:
        for i in range(v):
            print(res[i], end=' ')
        print()
        return
    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                check[i] = 1
                res[v] = i
                DFS(v + 1)
                check[i] = 0


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    res = [0] * n
    check = [0] * (n + 1)
    DFS(0)
