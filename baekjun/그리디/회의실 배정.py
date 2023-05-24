import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    meetings = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
    cnt = 1
    end_time = meetings[0][1]
    for i in range(1, n):
        if meetings[i][0] >= end_time:
            cnt += 1
            end_time = meetings[i][1]

    print(cnt)
