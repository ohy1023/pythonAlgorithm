N = int(input())
q = list(map(int,input().split()))

sum =0
count = 0
for i in q:
    if i==1:
        count+=1
        sum +=count
    else:
        count=0
print(sum)