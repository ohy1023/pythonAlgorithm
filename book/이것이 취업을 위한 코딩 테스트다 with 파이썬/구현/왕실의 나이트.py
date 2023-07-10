import sys

input = sys.stdin.readline

if __name__ == "__main__":
    coordinate = input().strip()
    row = int(coordinate[1])
    colum = int(ord(coordinate[0])) - 96

    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (1, 2)]

    cnt = 0

    for step in steps:
        nrow = row + step[0]
        ncolum = colum + step[1]

        if 1 <= nrow <= 8 and 1 <= ncolum <= 8:
            cnt += 1

    print(cnt)
