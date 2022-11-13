from collections import deque

n = int(input())
a = map(int, input().split())

a = deque(a)

answer = ""
temp = []

temp.append(0)

while a:
    if a[0] > temp[-1] and a[len(a) -1] > temp[-1]:
        if a[0] < a[len(a) -1]:
            temp.append(a.popleft())
            answer += "L"
        elif a[0] > a[len(a) -1]:
            temp.append(a.pop())
            answer += "R"
    elif a[0] > temp[-1]:
        temp.append(a.popleft())
        answer += "L"
    elif a[len(a) -1] > temp[-1]:
        temp.append(a.pop())
        answer += "R"
    elif a[0] < temp[-1] and a[len(a) -1] < temp[-1]:
        break

print(len(temp) -1)
print(answer)
