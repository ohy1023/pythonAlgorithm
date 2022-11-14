import math

def isPrime(x):
    if x == 1:
        return False
    for j in range(2, int(math.sqrt(x) + 1)):
        if x % j == 0:
            return False
    else:
        return True

n = int(input())

res = 0
while n > 0:
    a = n % 10
    res = res * 10 + a
    n //= 10

if isPrime(res):
    print("%d은 소수 맞음" % res)
else:
    print("%d은 소수 아님" % res)
