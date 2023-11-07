import sys


# 깊이 우선 탐색 (DFS) 함수
def dfs(x, y, maps, cnt, answer):
    # 목표 지점에 도달하면 최소 이동 횟수를 반환
    if x == len(maps) - 1 and y == len(maps[0]) - 1:
        return min(answer, cnt)

    # 이동 방향을 나타내는 리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 4방향에 대한 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 유효한 범위 내에 있고, 벽이 아닌 경우
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
            # 해당 위치를 방문했음을 표시
            maps[nx][ny] = 0
            # 재귀적으로 이동하며 최소 이동 횟수를 찾음
            answer = dfs(nx, ny, maps, cnt + 1, answer)
            # 다른 경로를 탐색하기 위해 다시 해당 위치를 방문하지 않았음을 표시
            maps[nx][ny] = 1

    return answer


def solution(maps):
    # 최소 이동 횟수를 나타내는 변수 초기화
    answer = float('inf')
    # 시작 위치를 방문한 것으로 표시
    maps[0][0] = 0
    # DFS 함수 호출
    result = dfs(0, 0, maps, 1, answer)

    # 도달할 수 없는 경우 -1 반환
    if result == float('inf'):
        return -1

    return result


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
