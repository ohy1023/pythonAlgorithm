import sys

"""
백준 1024 수열의 합 (실버 2) - 수학
https://www.acmicpc.net/problem/1024
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    N, L = map(int, input().split())

    # 가능한 수열의 길이 L부터 100까지 반복
    for i in range(L, 101):
        x = N - (i * (i + 1) / 2)

        # x가 i로 나누어 떨어지면 수열이 가능한 경우
        if x % i == 0:
            x = int(x / i)

            # x가 -1보다 크거나 같은 경우에 수열 출력
            if x >= -1:
                for j in range(1, i + 1):
                    print(x + j, end=' ')
                break
    else:
        # 모든 경우에 수열을 만들지 못한 경우 -1 출력
        print(-1)
