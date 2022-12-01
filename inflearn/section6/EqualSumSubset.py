import sys


def solution(v: int, answer: int):
    if total % 2 != 0:
        return
    if answer > total // 2:
        return
    if v == n:
        if answer == (total - answer):
            print("YES")
            sys.exit(0)
    else:
        solution(v + 1, answer + a[v])
        solution(v + 1, answer)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    solution(0, 0)
    print("NO")
