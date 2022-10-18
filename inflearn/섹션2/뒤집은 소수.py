def reverse(x):
    res = 0
    while x>0:
        res = res * 10 + (x%10)
        x //= 10
    return res

def isPrime(x):
    if x==1:
        return False
    for j in range(2, x//2+1):
        if (x % j == 0):
            return False
    else:
        return True


N = int(input())
numArr = list(map(int, input().split()))
for k in numArr:
    if (isPrime(reverse(k))):
        print(reverse(k), end=" ")

