from collections import deque

n, m = map(int, input().split())

patient = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]

patient = deque(patient)

cnt = 0

while True:
    cur = patient.popleft()
    if any(cur[1] < x[1] for x in patient):
        patient.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)
