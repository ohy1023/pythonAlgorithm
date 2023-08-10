import sys

input = sys.stdin.readline

# 유사 문제 : 백준 1463번 실버3

if __name__ == "__main__":
    x = int(input())
    dy = [0] * (x + 1)
    for i in range(2, x + 1):
        dy[i] = dy[i - 1] + 1
        if i % 5 == 0:
            dy[i] = min(dy[i], dy[i // 5] + 1)
        if i % 3 == 0:
            dy[i] = min(dy[i], dy[i // 3] + 1)
        if i % 2 == 0:
            dy[i] = min(dy[i], dy[i // 2] + 1)

    print(dy[x])
