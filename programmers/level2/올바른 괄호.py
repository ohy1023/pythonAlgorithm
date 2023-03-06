from collections import deque


def solution(s):
    dq = deque()
    if s[0] != "(":
        return False

    for i in s:
        if i == "(":
            dq.append(i)
        else:
            if len(dq) != 0:
                dq.pop()

    if len(dq) != 0:
        return False
    else:
        return True
