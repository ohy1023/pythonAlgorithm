n = int(input())
d = 2
while n != 1:
    if n % d != 0:
        d += 1
    else:
        n //= d
        print(d)
