import sys

"""
백준 14002 가장 긴 증가하는 부분 수열 4 (골드 4) - DP
https://www.acmicpc.net/problem/14002
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    dy = [0] * (n + 1)
    res = []
    dy[1] = 1
    for i in range(2, n + 1):
        max_length = 0
        for j in range(i - 1, 0, -1):
            if arr[j] < arr[i] and max_length < dy[j]:
                max_length = dy[j]
                idx = j
        dy[i] = max_length + 1

    max_length = max(dy)
    index = dy.index(max_length)
    while max_length > 0:
        res.append(arr[index])
        max_length -= 1
        while dy[index] != max_length:
            index -= 1

    res.reverse()

    print(len(res))
    print(*res)
