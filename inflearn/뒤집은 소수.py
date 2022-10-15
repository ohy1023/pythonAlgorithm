def reverse(x):
    strNum = str(x)[::-1]
    return int(strNum)


def isPrime(x):
    for j in range(2, x):
        if (x % j == 0):
            return False
    return True

N = int(input())
numArr = list(map(int, input().split()))
for k in numArr:
    if (isPrime(reverse(k))):
        print(reverse(k), end=" ")
