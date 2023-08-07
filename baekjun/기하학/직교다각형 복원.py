import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = [tuple(map(int, input().split())) for _ in range(n)]

    grouped_data_x = {}
    grouped_data_y = {}

    for x, y in nums:
        grouped_data_x.setdefault(x, []).append(y)
        grouped_data_y.setdefault(y, []).append(x)


    print(grouped_data_x)
    print(grouped_data_y)
    res = 0

    for x_coords in grouped_data_x.values():
        x_coords.sort()
        for i in range(len(x_coords) - 1, 0, -2):
            res += x_coords[i] - x_coords[i - 1]

    for y_coords in grouped_data_y.values():
        y_coords.sort()
        for i in range(len(y_coords) - 1, 0, -2):
            res += y_coords[i] - y_coords[i - 1]

    print(res)
