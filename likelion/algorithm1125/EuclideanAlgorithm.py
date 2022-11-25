def solution(a, b):
    if a % b == 0:
        return b
    return solution(b, a % b)


a, b = map(int, input().split())

print(solution(a, b))
