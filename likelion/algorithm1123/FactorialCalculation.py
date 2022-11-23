num = int(input())

def recursion(num):
    if num == 1:
        return 1

    return num * recursion(num-1)

print(recursion(num))