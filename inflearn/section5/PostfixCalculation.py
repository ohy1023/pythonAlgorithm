expression = input()

stack = []

for e in expression:
    if e.isdecimal():
        stack.append(int(e))
    else:
        second = stack.pop()
        first = stack.pop()
        if e == '*':
            answer = first * second
        elif e == '/':
            answer = first // second
        elif e == '+':
            answer = first + second
        elif e == '-':
            answer = first - second
        stack.append(answer)

print(answer)
