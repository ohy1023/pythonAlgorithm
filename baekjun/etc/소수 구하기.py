import sys

input = sys.stdin.readline

if __name__ == "__main__":
    m, n = map(int, input().split())
    nums = [1] * (n + 1)
    nums[0] = 0
    nums[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if nums[i] == 1:
            for j in range(i * i, n + 1, i):
                nums[j] = 0

    for k in range(m, n + 1):
        if nums[k] == 1:
            print(k)
