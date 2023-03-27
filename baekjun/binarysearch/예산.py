n = int(input())
requests = list(map(int, input().split()))
m = int(input())

lt, rt = 1, max(requests)
while lt <= rt:
    mid = (lt + rt) // 2
    res = 0
    for request in requests:
        if request >= mid:
            res += mid
        else:
            res += request

    if res > m:
        rt = mid - 1
    else:
        lt = mid + 1
print(rt)
