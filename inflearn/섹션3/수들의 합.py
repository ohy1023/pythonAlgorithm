n,m = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
for i in range(len(arr)):
    ans = 0
    for j in range(i+1,len(arr)+1):
        if sum(arr[i:j]) == m:
            cnt+=1
            break
print(cnt)