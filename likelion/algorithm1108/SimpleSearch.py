n = int(input())
arr = list(map(int,input().split()))
k = int(input())
cnt = -1

for i,a in enumerate(arr):
    if a == k:
        cnt = i+1
        break

print(cnt)