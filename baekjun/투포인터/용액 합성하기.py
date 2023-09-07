import sys

"""
백준 14921 용액 합성하기 (골드 5) - 투포인터
https://www.acmicpc.net/problem/14921
"""

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    liquids = list(map(int, input().split()))

    lt, rt = 0, n - 1
    res = int(1e9)

    while lt < rt:
        tmp = liquids[lt] + liquids[rt]

        if abs(tmp) < abs(res):
            res = tmp

            if res == 0:
                break

        if tmp < 0:
            lt += 1
        else:
            rt -= 1

    print(res)
