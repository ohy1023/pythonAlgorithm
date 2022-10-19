a = input()
ans =""
for i in a:
    if ord(i) < 65:
        ans+=i

cnt = 0
ans = int(ans)
for i in range(1,ans+1):
    if ans % i == 0:
        cnt+=1


print(ans)
print(cnt)