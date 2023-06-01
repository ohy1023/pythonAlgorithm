from typing import List


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    answer = []
    days = 0
    cnt = 0
    while len(progresses):
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                days += 1
    answer.append(cnt)
    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
