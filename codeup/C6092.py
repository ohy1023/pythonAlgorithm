n = int(input())
numArr = list(map(int,input().split()))
d = [0] * 23

for i in range(n):
  d[numArr[i]-1] +=1

for i in range(24):
  print(d[i],end=" ")



