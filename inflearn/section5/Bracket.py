brackets = input()
res = []
cnt = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        res.append(brackets[i])
    else:
        res.pop()
        if brackets[i - 1] == '(':
            cnt += len(res)
        else:
            cnt += 1

print(cnt)
