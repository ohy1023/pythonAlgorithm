import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    classes = [tuple(map(int, input().split())) for _ in range(n)]

    classes.sort()

    room = []

    heapq.heappush(room, classes[0][1])

    for i in range(1, n):
        if classes[i][0] < room[0]:
            heapq.heappush(room, classes[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, classes[i][1])

    print(len(room))
