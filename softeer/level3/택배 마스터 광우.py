"""
레일의 순서를 바꿔 가면서
k 번 일했을 떄 값의 최소를 찾아내서 출력

how?
어떻게 레일의 순서를 바꾸지
조합을 통해 경우의 수
"""

import sys
from itertools import permutations

input = sys.stdin.readline


def move(x, n):
    return (x + 1) % n


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    lines = list(map(int, input().split()))
    permutation_info = list(map(list, permutations(lines)))

    res = 2_147_000_000

    for permutation in permutation_info:
        i = 0
        cart = 0
        cnt = 0
        tmp = 0
        while True:
            if cnt == k:
                if res > tmp:
                    res = tmp
                break
            if cart + permutation[i] > m:
                cnt += 1
                tmp += cart
                cart = permutation[i]
            else:
                cart += permutation[i]
            i = move(i, n)

    print(res)
