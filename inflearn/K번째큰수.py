from random import random

N,K = map(int,input().split())

x = list(map(int,input().split()))

res = set()

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res.add(x[i]+x[j]+x[k])

res=list(res)
res.sort(reverse=True)

print(res[K-1])
random