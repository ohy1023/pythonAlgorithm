import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    cards = sorted(list(map(int, input().split())))
    m = int(input())
    requests = list(map(int, input().split()))

    cnt = {}
    for card in cards:
        if card in cnt:
            cnt[card] += 1
        else:
            cnt[card] = 1

    print(' '.join(str(cnt[r]) if r in cnt else '0' for r in requests))
