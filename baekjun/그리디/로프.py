import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    ropes = sorted(list(int(input()) for _ in range(n)))
    if n == 1:
        print(ropes[-1])
    else:
        res = 0
        for i in range(2, n + 1):
            tmp = ropes[-i] * i
            if res < tmp:
                res = tmp
        print(res)
