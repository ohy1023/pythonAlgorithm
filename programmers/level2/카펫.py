def solution(brown, yellow):
    answer = []
    total = brown + yellow  # a * b = total
    for b in range(3, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [a, b]

    return answer


print(solution(10, 2))
