from collections import deque


def bfs(x, y, maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dq = deque()

    dq.append((x, y))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                dq.append((nx, ny))

    return maps[len(maps) - 1][len(maps[0]) - 1]


def solution(maps):
    answer = bfs(0, 0, maps)

    # BFS 함수 호출
    return -1 if answer == 1 else answer


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
