def push(a, num):
    a.append(num)


def pop(a):
    if len(a) == 0:
        print(-1)
    else:
        print(stack.pop())


def size(a):
    print(len(a))


def empty(a):
    if len(a) == 0:
        print(1)
    else:
        print(0)


def top(a):
    if len(a) == 0:
        print(-1)
    else:
        print(a[-1])


import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    functions = sys.stdin.readline().split()

    if functions[0] == 'push':
        push(stack, functions[1])
    elif functions[0] == 'pop':
        pop(stack)
    elif functions[0] == 'size':
        size(stack)
    elif functions[0] == 'empty':
        empty(stack)
    elif functions[0] == 'top':
        top(stack)
