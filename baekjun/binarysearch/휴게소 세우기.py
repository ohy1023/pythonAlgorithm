import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m, l = map(int, input().split())
    rest_area = [0] + list(map(int, input().split())) + [l]
    rest_area.sort()

    res = 0
    lt, rt = 1, l
    while lt <= rt:
        count = 0
        mid = (lt + rt) // 2
        for i in range(len(rest_area) - 1):
            if rest_area[i + 1] - rest_area[i] > mid:
                count += (rest_area[i + 1] - rest_area[i] - 1) // mid

        if count > m:
            lt = mid + 1
        else:
            rt = mid - 1
            res = mid

    print(res)
