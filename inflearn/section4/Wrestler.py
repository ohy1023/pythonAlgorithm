n = int(input())
player = []
for _ in range(n):
    c,k = map(int,input().split())
    player.append((c,k))

player.sort(reverse=True)

largest = 0
cnt = 0
for x,y in player:
    if y > largest:
        largest = y
        cnt+=1

print(cnt)