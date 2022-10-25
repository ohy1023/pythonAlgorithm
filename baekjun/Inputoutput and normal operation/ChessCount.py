chessCount = [1,1,2,2,2,8]
a = list(map(int,input().split()))

for i in range(6):
    print(chessCount[i] - a[i],end=" ")