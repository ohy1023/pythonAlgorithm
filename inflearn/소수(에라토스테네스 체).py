import sys

def isPrime(n):
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

N = int(sys.stdin.readline())
count =0
for j in range(2,N+1):
    if isPrime(j):
        count+=1
print(count)

