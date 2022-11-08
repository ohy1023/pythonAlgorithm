n ,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

lt = 0
rt = len(arr) - 1
res = -1
while lt <= rt:
    mid = (lt + rt) // 2
    if arr[mid] == k:
        res = mid + 1
        break
    elif arr[mid] > k:
        rt = mid -1
    else:
        lt = mid + 1
print(res)
