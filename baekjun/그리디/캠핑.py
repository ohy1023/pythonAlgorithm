import sys

input = sys.stdin.readline

if __name__ == "__main__":
    cnt = 0
    while True:
        l, p, v, = map(int, input().split())
        cnt += 1
        if l == p == v == 0:
            break
        res = min(l, v % p) + l * (v // p)
        print("Case %d: %d" % (cnt, res))
