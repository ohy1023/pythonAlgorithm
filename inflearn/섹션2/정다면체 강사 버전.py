N,M = map(int,input().split())
count = [0 for i in range(N+M+1)]
for a in range(1,N+1):
    for b in range(1,M+1):
        count[a+b] +=1

for idx,c in enumerate(count):
    if c==max(count):
        print(idx,end=" ")