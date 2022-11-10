n = int(input())
box = list(map(int, input().split()))
k = int(input())

for _ in range(k):
    maxIdx = box.index(max(box))
    box[maxIdx] -= 1
    minIdx = box.index(min(box))
    box[minIdx] += 1

print(max(box) - min(box))
