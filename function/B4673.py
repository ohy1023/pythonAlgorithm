def d(n):
    sum = 0
    origin = n
    while (n > 0):
        sum += n % 10
        n //= 10
    return sum + origin

arr = list(range(1,10001))
remove_list = []
for a in arr:
    if (d(a) <= 10000):
        remove_list.append(d(a))

for remove_num in set(remove_list):
    arr.remove(remove_num)
for self_num in arr:
    print(self_num)