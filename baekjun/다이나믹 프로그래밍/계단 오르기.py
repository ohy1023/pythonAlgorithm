import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    dy = [0] * n
    if n <= 2:  # 계단이 2개 이하 일 경우
        print(sum(stairs))
    else:
        dy[0] = stairs[0]
        dy[1] = stairs[0] + stairs[1]
        dy[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
        for i in range(3, n):
            dy[i] = max(dy[i - 2] + stairs[i], dy[i - 3] + stairs[i - 1] + stairs[i])
        print(dy[n - 1])
