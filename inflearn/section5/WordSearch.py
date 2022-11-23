from collections import deque

n = int(input())

note = [input() for _ in range(n)]
use = [input() for _ in range(n-1)]

dp = deque(note)

while len(dp) != 0:
    word = dp.popleft()
    if word not in use:
        print(word)
        break
