import sys

input = sys.stdin.readline


def DFS(v, t):
    global cnt
    if v == n:
        return
    if t + nums[v] == s:
        cnt += 1
    DFS(v + 1, t + nums[v])
    DFS(v + 1, t)


if __name__ == "__main__":
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    DFS(0, 0)
    print(cnt)
