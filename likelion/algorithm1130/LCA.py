def solution(a: int, b: int) -> int:
    if a > b:
        return solution(a // 2, b) + 1
    elif a < b:
        return solution(a, b // 2) + 1
    else:
        return 0


a, b = map(int, input().split())
print(solution(a, b))
