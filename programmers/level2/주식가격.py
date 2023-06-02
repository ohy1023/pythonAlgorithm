from typing import List
from collections import deque


def solution(prices: List[int]) -> List[int]:
    answer = []
    dq = deque(prices)
    while dq:
        price = dq.popleft()
        sec = 0
        for q in dq:
            sec += 1
            if price > q:
                break
        answer.append(sec)

    return answer


def solution2(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if not stack:
            while stack and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer


if __name__ == "__main__":
    print(solution2([1, 2, 3, 2, 3]))
