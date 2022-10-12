x = int(input())
for _ in range(x):
    arr =list(map(int,input().split()))
    cnt = arr[0]
    meanCnt = 0
    score = arr[1:]
    mean = sum(score) / cnt
    for j in score:
        if j > mean:
            meanCnt+=1
    print("{0:0.3f}%".format(meanCnt/cnt*100))





