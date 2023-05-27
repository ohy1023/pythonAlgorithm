import math


def is_prime(x: int) -> bool:
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def convert(n: int, base: int) -> str:
    rev_base = ''

    while n:
        n, mod = divmod(n, base)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n: int, k: int) -> int:
    answer = 0
    split = convert(n, k).split('0')

    for s in split:
        if not s:
            continue
        if is_prime(int(s)):
            answer += 1
    return answer


print(solution(437674, 3))
