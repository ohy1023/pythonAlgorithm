from collections import deque

n, k = map(int, input().split())

prince = list(range(1, n + 1))

prince = deque(prince)

cnt = 0

while len(prince) != 1:

    cnt += 1

    if cnt == k:
        prince.popleft()
        cnt = 0

    else:
        prince.append(prince.popleft())

print(prince.popleft())
