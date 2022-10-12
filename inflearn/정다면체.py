N,M = map(int,input().split())
x= []
for a in range(1,N+1):
    for b in range(1,M+1):
        x.append(a+b)
x.sort()
max = 0
for i in range(2,N+M+1):
    if max <= x.count(i):
        max = x.count(i)

maxCount = set()
for j in x:
    if max == x.count(j):
        maxCount.add(j)

for k in maxCount:
    print(k,end=" ")