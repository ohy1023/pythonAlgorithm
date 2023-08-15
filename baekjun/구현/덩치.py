import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    bodies = [tuple(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        res = 1
        cur_x, cur_y = bodies[i][0], bodies[i][1]
        for j in range(n):
            if i == j:
                continue
            other_x, other_y = bodies[j][0], bodies[j][1]
            if cur_x < other_x and cur_y < other_y:
                res += 1

        print(res, end=" ")
