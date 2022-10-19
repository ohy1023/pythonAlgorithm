a = input()
res=0
for i in a:
    if i.isdecimal():
        res=res*10+int(i)

cnt = 0
for i in range(1,res+1):
    if res % i == 0:
        cnt+=1

print(res)
print(cnt)