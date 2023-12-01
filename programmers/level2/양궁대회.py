from copy import deepcopy


def solution(n, info):
    answer = []
    max_diff = 0

    def calcDiff(info, shoot):
        peach_score, lion_score = 0, 0

        for i in range(11):
            if info[i] == 0 and shoot[i] == 0:
                continue
            if info[i] < shoot[i]:
                lion_score += (10 - i)
            else:
                peach_score += (10 - i)

        return lion_score - peach_score

    def dfs(info, shoot, n, v):
        nonlocal max_diff, answer
        if v == 11:
            if n != 0:
                shoot[10] = n
            score_diff = calcDiff(info, shoot)

            if score_diff <= 0:
                return

            result = deepcopy(shoot)

            if score_diff > max_diff:
                max_diff = score_diff
                answer = [result]
                return

            if score_diff == max_diff:
                answer.append(result)
            return

        if info[v] < n:
            shoot.append(info[v] + 1)
            dfs(info, shoot, n - info[v] - 1, v + 1)
            shoot.pop()

        shoot.append(0)
        dfs(info, shoot, n, v + 1)
        shoot.pop()

    dfs(info, [], n, 0)

    if not answer:
        return [-1]

    answer.sort(key=lambda x: x[::-1], reverse=True)

    return answer[0]


"""
프로그래머스 양궁대회 (Level.2) - DFS
https://school.programmers.co.kr/learn/courses/30/lessons/92342
"""

if __name__ == "__main__":
    print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
