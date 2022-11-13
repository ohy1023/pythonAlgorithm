n = int(input())
fear = list(map(int, input().split()))
fear.sort()

groupNum = 0
cnt = 0
for i in fear:
    cnt += 1
    if cnt >= i:
        groupNum += 1
        cnt = 0

print(groupNum)
