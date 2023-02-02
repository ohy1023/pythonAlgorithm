import sys

input = sys.stdin.readline
n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

lt = 1
rt = house[-1] - house[0]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    start = house[0]
    cnt = 1
    for i in range(1, len(house)):
        if house[i] >= start + mid:
            start = house[i]
            cnt += 1
    if cnt < c:
        rt = mid - 1
    else:
        lt = mid + 1
        res = mid

print(res)
