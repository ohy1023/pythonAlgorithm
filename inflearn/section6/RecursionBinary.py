def solution(n: int):
    if n > 0:
        solution(n // 2)
        print(str(n % 2), end="")


solution(int(input()))
