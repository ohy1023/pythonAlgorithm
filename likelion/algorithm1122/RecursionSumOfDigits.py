def solution(num: int) -> int:
    if num <= 0:
        return 0
    res = num % 10
    num //= 10

    return res + solution(num)


num = int(input())
print(solution(num))
