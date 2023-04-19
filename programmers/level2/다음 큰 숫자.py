def cnt_one(n):
    return bin(n)[2:].count('1')


def solution(n):
    baseline = cnt_one(n)
    res = n + 1
    while cnt_one(res) != baseline:
        res += 1
    return res


print(solution(15))
