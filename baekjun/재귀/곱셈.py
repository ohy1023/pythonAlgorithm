import sys

input = sys.stdin.readline


def DAC(a, b):
    global tmp
    if b == 1:
        return a % c
    else:
        tmp = DAC(a, b // 2)
        if b % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(DAC(a, b))
