def printRow(n : int):
    if n == 0:
        return
    printRow(n-1)
    print(n,end=" ")


def solution(n : int):
    if n == 0:
        return
    solution(n-1)
    printRow(n)
    print()

n = int(input())

solution(n)