import sys

"""
백준 2502 떡 먹는 호랑이 (실버 1) - DP
https://www.acmicpc.net/problem/2502
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    d, k = map(int, input().split())

    dy = [0] * 31
    dy[1], dy[2] = 1, 1

    while True:
        for i in range(3, d + 1):
            dy[i] = dy[i - 2] + dy[i - 1]

        if dy[d] == k:
            print(dy[1], dy[2], sep="\n")
            break
        elif dy[d] < k:
            dy[2] += 1
        else:
            dy[1] += 1
            dy[2] = dy[1]
