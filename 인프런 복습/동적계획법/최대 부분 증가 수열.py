import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    dy = [0] * (n + 1)
    dy[1] = 1
    for i in range(2, n + 1):
        max_length = 0
        for j in range(i - 1, 0, -1):
            if arr[j] < arr[i] and max_length < dy[j]:
                max_length = dy[j]
        dy[i] = max_length + 1

    print(max(dy))
