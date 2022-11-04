def Count(capacity):
    cnt = 1
    sum = 0
    for x in minute:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
minute = list(map(int, input().split()))

largest = max(minute)
lt = 1
rt = sum(minute)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= largest and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)