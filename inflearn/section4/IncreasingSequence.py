
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1

baseLine = 0
answer = ""
temp = []
while lt <= rt:
    if baseLine < a[lt]:
        temp.append((a[lt], 'L'))

    if baseLine < a[rt]:
        temp.append((a[rt], 'R',))

    temp.sort()
    if len(temp) == 0:
        break
    else:
        answer += temp[0][1]
        baseLine = temp[0][0]
        if temp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    temp.clear()
print(len(answer))
print(answer)
