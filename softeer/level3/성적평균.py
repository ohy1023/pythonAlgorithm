import sys

input = sys.stdin.readline


def custom_round(number, decimal_places=0):
    return int(number * 10 ** decimal_places + (0.5 if number >= 0 else -0.5)) / (10 ** decimal_places)


if __name__ == "__main__":

    n, k = map(int, input().split())
    scores = list(map(int, input().split()))

    for _ in range(k):
        s, e = map(int, input().split())
        res = sum(scores[s - 1:e]) / (e - s + 1)
        print("%0.2f" % custom_round(res, 2))
