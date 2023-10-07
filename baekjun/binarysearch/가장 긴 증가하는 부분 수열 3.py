import sys

"""
백준 12738 가장 긴 증가하는 부분 수열 3 (골드 2) - 이진탐색
https://www.acmicpc.net/problem/12738
"""

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    sequence = list(map(int, input().split()))
    res = [-1_000_000_001]

    for s in sequence:
        if res[-1] < s:
            res.append(s)
        else:
            lt = 1
            rt = len(res)

            while lt < rt:
                mid = (lt + rt) // 2

                if res[mid] < s:
                    lt = mid + 1
                else:
                    rt = mid

            res[rt] = s

    print(len(res) - 1)
