def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

N = int(input())
x = list(map(int,input().split()))

max = -2147000000
for i in x:
    if max < digit_sum(i):
        max = digit_sum(i)
        res = i

print(res)



