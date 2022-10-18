# 1. 계산
# 2. 입력값으로 반복

def getReward(a,b,c):
    if a==b==c :
        return 10000+a*1000
    elif a==c or a==b:
        return 1000 + a * 100
    elif b==c:
        return 1000 + b * 100
    else:
        return max(a,b,c) *100

n = int(input())
maxReward = -2147000000
for i in range(n):
    a,b,c = map(int,input().split())
    if maxReward < getReward(a,b,c):
        maxReward = getReward(a, b, c)

print(maxReward)





