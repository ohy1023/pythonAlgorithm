def Count(len):
    cnt = 1
    ep = horse[0]
    for i in range(1, n):
        if horse[i] - ep >= len:
            cnt += 1
            ep = horse[i]
    return cnt


n, c = map(int, input().split())
horse = list(int(input()) for _ in range(n))
horse.sort()

lt = 1
rt = horse[n - 1]
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)

