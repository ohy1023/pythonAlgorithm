a = input()
b = input()

sd = dict()

for x in a:
    sd[x] = sd.get(x, 0) + 1

for x in b:
    sd[x] = sd.get(x, 0) - 1

if any(sd.values()) != 0:
    print("NO")
else:
    print("YES")