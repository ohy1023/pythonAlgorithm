import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    students = sorted(list(map(int, input().split())))

    cost = []
    for i in range(1, len(students)):
        cost.append(students[i] - students[i - 1])
    cost.sort()
    res = 0
    for i in range(n - k):
        c = cost[i]
        res += c

    print(res)

