import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())), reverse=True)

    res = 0
    cnt = m // (k + 1) * k
    cnt += m % (k + 1)

    res += nums[0] * cnt + (m - cnt) * nums[1]

    print(res)
