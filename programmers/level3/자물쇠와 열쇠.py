from copy import deepcopy

"""
프로그래머스 level 3 자물쇠와 열쇠 - 구현
https://school.programmers.co.kr/learn/courses/30/lessons/60059?language=python3
"""


def rotate(arr):
    return list(zip(*arr[::-1]))


def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]


def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[i + M][j + M] != 1:
                return False
    return True


def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (N * 3) for _ in range(N * 3)]

    for i in range(N):
        for j in range(N):
            board[i + M][j + M] = lock[i][j]

    rotated_key = deepcopy(key)
    for _ in range(4):
        rotated_key = rotate(rotated_key)

        for x in range(M + N):
            for y in range(M + N):
                attach(x, y, M, rotated_key, board)

                if check(board, M, N):
                    return True

                detach(x, y, M, rotated_key, board)

    return False


if __name__ == "__main__":
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
