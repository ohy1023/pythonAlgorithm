a,b,c, = map(int,input().split())
count = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k,sep=" ")
            count+=1


print(count)