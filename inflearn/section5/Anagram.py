a = input()
b = input()

sd = dict()

for x in a:
    sd[x] = sd.get(x, 0) + 1

for x in b:
    sd[x] = sd.get(x, 0) - 1

for x in sd.values():
    if x != 0:
        print("NO")
        break
else:
    print("YES")
