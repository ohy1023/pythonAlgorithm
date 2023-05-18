import sys

input = sys.stdin.readline


def binary_search():
    global res, ans1, ans2
    lt, rt = i + 1, n - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        temp = liquids[i] + liquids[mid]

        if abs(temp) <= res:
            res = abs(temp)
            ans1, ans2 = i, mid

            if temp == 0:
                break
        if temp < 0:
            lt = mid + 1
        else:
            rt = mid - 1


if __name__ == "__main__":
    n = int(input())
    liquids = list(map(int, input().split()))
    res = float("INF")
    ans1, ans2 = 0, 0
    for i in range(n - 1):
        binary_search()

    print(liquids[ans1], liquids[ans2])
