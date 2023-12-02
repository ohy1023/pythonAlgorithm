def check_pillar(x, y, pillar, bar):
    if y == 0 or pillar[x][y - 1]:
        return True

    if (x > 0 and bar[x - 1][y]) or bar[x][y]:
        return True

    return False


def check_bar(x, y, pillar, bar):
    if pillar[x][y - 1] or pillar[x + 1][y - 1]:
        return True
    if x > 0 and bar[x - 1][y] and bar[x + 1][y]:
        return True

    return False


def can_delete(x, y, pillar, bar):
    for i in range(x - 1, x + 2):
        for j in range(y, y + 2):
            if pillar[i][j] and check_pillar(i, j, pillar, bar) == False:
                return False
            if bar[i][j] and check_bar(i, j, pillar, bar) == False:
                return False
    return True


def solution(n, build_frame):
    pillar = [[0] * (n + 2) for _ in range(n + 2)]
    bar = [[0] * (n + 2) for _ in range(n + 2)]

    for x, y, kind, cmd in build_frame:

        if kind == 0:
            if cmd == 1:
                if check_pillar(x, y, pillar, bar):
                    pillar[x][y] = 1
            else:
                pillar[x][y] = 0
                if not can_delete(x, y, pillar, bar):
                    pillar[x][y] = 1
        else:
            if cmd == 1:
                if check_bar(x, y, pillar, bar):
                    bar[x][y] = 1
            else:
                bar[x][y] = 0
                if not can_delete(x, y, pillar, bar):
                    bar[x][y] = 1

    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if pillar[x][y]:
                answer.append([x, y, 0])
            if bar[x][y]:
                answer.append([x, y, 1])

    return answer


"""
프로그래머스 level 3 기둥과 보 설치 - 구현
https://school.programmers.co.kr/learn/courses/30/lessons/60061?language=python3
"""

if __name__ == "__main__":
    print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                       [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
