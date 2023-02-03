import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

lt = 1
rt = n * n
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)

    if cnt >= k:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
