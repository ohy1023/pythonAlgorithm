import sys

input = sys.stdin.readline


def DFS(v):
    global res
    if v == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        return
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                res[v] = nums[i]
                DFS(v + 1)
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    check = [0] * n
    res = [0] * m
    DFS(0)
