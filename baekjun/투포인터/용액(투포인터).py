import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    liquids = list(map(int, input().split()))
    liquids.sort()

    lt, rt = 0, n - 1
    min_res = abs(liquids[lt] + liquids[rt])
    res1, res2 = lt, rt

    while lt < rt:
        temp = liquids[lt] + liquids[rt]

        if abs(temp) <= min_res:
            res1, res2 = lt, rt
            min_res = abs(temp)

            if min_res == 0:
                break
        if temp < 0:
            lt += 1
        else:
            rt -= 1
    print(liquids[res1], liquids[res2])
