def solution(n: int):
    if n == 0:
        return
    solution(n // 2)
    print(n % 2, end="")


solution(int(input()))
