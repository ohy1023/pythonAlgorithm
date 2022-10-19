a,m,d,n = map(int,input().split())

ans = a
for i in range(n-1):
    ans = ans * m + d

print(ans)