N = int(input())
temp = N;
cnt = 0
while True:
    N = ((N % 10)*10) + (((N // 10) +(N % 10) )% 10)
    cnt += 1
    if temp == N:
        print(cnt)
        break


