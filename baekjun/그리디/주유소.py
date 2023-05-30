import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dist = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    min_cost = cost[0]
    answer = 0

    for i in range(n - 1):
        if min_cost > cost[i]:
            min_cost = cost[i]
        answer += min_cost * dist[i]

    print(answer)
