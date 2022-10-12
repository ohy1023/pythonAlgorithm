import sys

n,k = map(int,sys.stdin.readline().split())
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count+=1
    if count == k:
        print(i)
        break
else:
    print(-1)


# 숫자 입력 받음
# 약수