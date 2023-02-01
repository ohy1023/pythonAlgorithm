n, m = map(int, input().split())
trees = list(map(int, input().split()))

lt, et = 1, max(trees)

while lt <= et:
    mid = (lt + et) // 2
    res = 0
    for i in trees:
        if i >= mid:
            res += i - mid
    if res >= m:
        lt = mid + 1
    else:
        et = mid - 1
print(et)
