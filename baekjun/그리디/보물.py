import sys
from typing import List

input = sys.stdin.readline


# 간단한 풀이 ( 배열 b를 재배열 하지 말라는 규칙 위반)
def sol_simple(a: List[int], b: List[int]) -> int:
    a.sort()
    b.sort(reverse=True)
    return sum(a[i] * b[i] for i in range(n))


# 정답 풀이 (배열 b를 재배열하지 않는 풀이)
def sol_standard(a: List[int], b: List[int]) -> int:
    a.sort()
    res = 0
    for num in a:
        res += num * b.pop(b.index(max(b)))
    return res


if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    print(sol_simple(a_list, b_list))

    print(sol_standard(a_list, b_list))
