import math


def solution(n, k):
    answer = []
    a = list(range(1, n + 1))

    while k > 1:
        fac = math.factorial(len(a) - 1)
        answer.append(a.pop((k - 1) // fac))
        print(answer)
        k = k - (fac * ((k - 1) // fac))
        print(k)
    return answer + a
