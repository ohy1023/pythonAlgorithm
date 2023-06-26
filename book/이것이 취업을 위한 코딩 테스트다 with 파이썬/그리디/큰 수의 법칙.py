import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())), reverse=True)

    res = 0
    cnt = 0

    while True:
        for i in range(k):
            if cnt == m:
                break
            res += nums[0]
            cnt += 1

        if cnt == m:
            break
        res += nums[1]
        cnt += 1

    print(res)
