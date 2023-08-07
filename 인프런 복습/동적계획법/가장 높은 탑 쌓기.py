import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    boxes = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: -x[0])
    dy = [0] * n
    dy[0] = boxes[0][1]
    res = boxes[0][1]
    for i in range(1, n):
        max_height = 0
        for j in range(i - 1, -1, -1):
            if boxes[i][2] < boxes[j][2] and max_height < dy[j]:
                max_height = dy[j]

        dy[i] = max_height + boxes[i][1]
        res = max(res, dy[i])
    print(res)
