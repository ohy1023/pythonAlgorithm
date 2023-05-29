from collections import Counter
from functools import reduce


def solution(clothes):
    counter = Counter(list(type for clothe, type in clothes))
    print(counter)

    ans = reduce(lambda acc, cur: acc * (cur + 1), counter.values(), 1)
    print(ans)

    return ans - 1


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
