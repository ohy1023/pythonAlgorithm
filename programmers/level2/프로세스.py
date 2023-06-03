from typing import List
from collections import deque


def solution(priorities: List[int], location: int) -> int:
    answer = 0
    dq = deque([(i, p) for i, p in enumerate(priorities)])
    while True:
        cur = dq.popleft()
        if any(cur[1] < q[1] for q in dq):
            dq.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
