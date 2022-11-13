# 에라토스테네스의 체
# 50까지 중 소수 출력하기
import math


def solution(n):
    cnt = 0
    ch = [0] * (n + 1)
    for i in range(2, n + 1):
        if ch[i] == 0:
            cnt += 1
            for j in range(i, n + 1, i):
                ch[j] = 1
    return cnt

print(solution(50))