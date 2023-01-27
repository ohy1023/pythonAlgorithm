def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y - 1 >= 0 and board[x][y - 1] == 1 and ch[x][y - 1] == 0:
            DFS(x, y - 1)
        elif y + 1 < 10 and board[x][y + 1] == 1 and ch[x][y + 1] == 0:
            DFS(x, y + 1)
        else:
            DFS(x - 1, y)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    print(board)
    for i in range(10):
        if board[9][i] == 2:
            DFS(9, i)
