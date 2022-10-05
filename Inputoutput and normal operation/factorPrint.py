# N의 약수 출력

N = int(input())

for i in range(1,N+1):
    if N % i == 0:
        print(i)