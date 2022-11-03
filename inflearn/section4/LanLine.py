k,n = map(int,input().split())
a = [int(input()) for _ in range(k)]
x = list()

for j in range(1,max(a)):
    ans = 0
    for i in a:
        ans += i//j
    if ans == n:
        x.append(j)

print(max(x))


# 4 11
# 802
# 743
# 457
# 539