def cnt(len):
    cnt = 0
    for i in line:
        cnt += i//len
    return cnt

k,n = map(int,input().split())
line = [int(input()) for _ in range(k)]
largest = max(line)
res = 0

lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt) // 2
    if cnt(mid) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid -1

print(res)