
k = int(input())
a = list(map(int, input().split()))

answer = [0] * k

for i in range(k):
    for j in range(k):
        if a[i] == 0 and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            a[i] -= 1

for i in answer:
    print(i, end=" ")
