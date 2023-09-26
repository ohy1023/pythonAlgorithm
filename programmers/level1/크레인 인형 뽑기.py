"""
프로그래머스 크레인 인형 뽑기 (Level.1) - 스택
https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""


def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                tmp = board[i][move - 1]
                board[i][move - 1] = 0
                if len(stack) != 0 and stack[-1] == tmp:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(tmp)
                break

    return answer


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    print(solution(board, moves))
