import sys

input = sys.stdin.readline

m, n, k = map(int, input().split())
secret = list(map(int, input().split()))
button = list(map(int, input().split()))

if m > n:
    print("normal")
else:
    for i in range(n - m + 1):
        if secret == button[i:i + m]:
            print("secret")
            break
    else:
        print("normal")
