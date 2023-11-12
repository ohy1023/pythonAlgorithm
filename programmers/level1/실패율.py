def solution(N, stages):
    answer = []
    total = len(stages)
    for i in range(1, N + 1):
        if total != 0:
            p = stages.count(i) / total
            total -= stages.count(i)
            answer.append((i, p))
        else:
            answer.append((i, 0))

    answer.sort(key=lambda x: (-x[1], x[0]))

    return [item[0] for item in answer]


"""
프로그래머스 실패율 (Level.1) - 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/42889
"""

if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
