import sys

input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))

for r in requests:
    if r not in cards:
        print(0, end=' ')
    else:
        print(1, end=' ')
