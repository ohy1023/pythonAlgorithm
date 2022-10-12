N = int(input())
x = list(map(int,input().split()))

mean = int((sum(x) / N) + 0.5)
min = 2147000000
for idx,a in enumerate(x):
    tmp = abs(a-mean)
    if tmp < min:
        min = tmp
        score = a
        res =idx+1
    elif tmp == min:
        if a > score:
            score = a;
            res = idx+1

print(mean, res,sep=" ")
