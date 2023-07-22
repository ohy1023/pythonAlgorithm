n, k = map(int, input().split())
list_a = sorted(list(map(int, input().split())))
list_b = sorted(list(map(int, input().split())), reverse=True)

for i in range(n):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else:
        break

print(sum(list_a))
