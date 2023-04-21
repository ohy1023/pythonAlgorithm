def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])  # stack이 비어있다면 push()
        else:
            if s[i] == stack[-1]:  # stack 마지막 값과 s[i]가 같다면 pop()
                stack.pop()
            else:
                stack.append(s[i])  # stack 마지막 값과 s[i]가 다르면 push()

    if not stack:
        return 1  # stack이 비어있다면 return 1
    else:
        return 0  # stack이 비어있지 않다면 return 0


def solution2(s):  # 시간 초과
    start = 0
    while start < len(s) - 1:
        if s[start] == s[start + 1]:
            s = s.replace(s[start] + s[start], '')
            start = max(0, start - 1)
        else:
            start += 1
    if len(s) == 0:
        return 1
    else:
        return 0

print(solution('cdcd'))
