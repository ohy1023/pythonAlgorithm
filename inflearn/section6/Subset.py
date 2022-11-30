def solution(v: int):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        ch[v] = 1
        solution(v + 1)
        ch[v] = 0
        solution(v + 1)


n = int(input())
ch = [0] * (n + 1)
solution(1)
