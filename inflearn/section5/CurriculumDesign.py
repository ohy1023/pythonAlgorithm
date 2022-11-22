from collections import deque

need = input()
n = int(input())

for i in range(1, n + 1):

    dp = deque(need)
    plan = input()
    for x in plan:
        if x in dp:
            if x != dp.popleft():
                print(f"#{i} NO")
                break
    else:
        if len(dp) == 0:
            print(f"#{i} YES")
        else:
            print(f"#{i} NO")
