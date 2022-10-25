cnt = int (input())
score = list(map(int,input().split()))
sum = 0
max = max(score)
for x in score:
    sum += x / max * 100
print(sum / cnt)
