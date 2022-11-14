n, m = map(int, input().split())

a = []

while n > 0:
    a.append(n % 10)
    n //= 10

a.reverse()
cnt = 0
while cnt != m:
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            cnt += 1
            a.pop(i)
            break
    else:
        for i in range(m - cnt):
            a.pop()
        break
for i in a:
    print(i, end="")
