def solution(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1

    return solution(num - 1) + solution(num - 2)


num = int(input())

print(solution(num))
