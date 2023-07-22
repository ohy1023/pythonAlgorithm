import sys

input = sys.stdin.readline


def check():
    bingo = 0

    # 행 체크
    for i in range(5):
        if board[i].count(0) == 5:
            bingo += 1

    # 열 체크
    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += board[j][i]
        if tmp == 0:
            bingo += 1

    # 대각선 체크
    tmp2 = 0
    for k in range(5):
        tmp2 += board[k][k]
    if tmp2 == 0:
        bingo += 1

    tmp3 = 0
    for m in range(5):
        tmp3 += board[m][4 - m]
    if tmp3 == 0:
        bingo += 1

    return bingo


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(5)]
    answer = [list(map(int, input().split())) for _ in range(5)]

    cnt = 0
    for i in range(5):
        for n in range(5):
            for j in range(5):
                for k in range(5):
                    if answer[i][n] == board[j][k]:
                        board[j][k] = 0
                        cnt += 1

                    if cnt >= 12:
                        if check() >= 3:
                            print(cnt)
                            exit()
