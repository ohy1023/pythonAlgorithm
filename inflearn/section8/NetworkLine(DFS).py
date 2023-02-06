import sys


def DFS(num):
    if dy[num] > 0:
        return dy[num]
    if num == 1 or num == 2:
        return num
    else:
        dy[num] = DFS(num - 2) + DFS(num - 1)
        return dy[num]


input = sys.stdin.readline

n = int(input())
dy = [0] * (n + 1)

print(DFS(n))
