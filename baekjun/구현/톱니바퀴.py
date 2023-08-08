import sys
from collections import deque

if __name__ == "__main__":

    input = sys.stdin.readline
    arr = [deque(list(map(int, input().strip()))) for _ in range(4)]
    k = int(input())
    for _ in range(k):
        r = []  # ✨ 처음 톱니 상태 저장
        for i in range(4):
            r.append([arr[i][6], arr[i][2]])
        n, d = map(int, input().split())
        n -= 1

        if n != 0:
            for i in range(n, 0, -1):
                if r[i][0] != r[i - 1][1]:
                    if (n - (i - 1)) % 2 == 0:
                        arr[i - 1].rotate(d)
                    elif (n - (i - 1)) % 2 != 0:
                        arr[i - 1].rotate(-1 * d)
                elif r[i][0] == r[i - 1][1]:
                    break
                # ✨ 오른쪽에 있는 톱니들 돌리기
        if n != 3:
            for i in range(n, 3):
                if r[i][1] != r[i + 1][0]:
                    if (n - (i + 1)) % 2 == 0:
                        arr[i + 1].rotate(d)
                    elif (n - (i + 1)) % 2 != 0:
                        arr[i + 1].rotate(-1 * d)
                elif r[i][1] == r[i + 1][0]:
                    break
        arr[n].rotate(d)

        # ✨ 출력
    res = 0
    if arr[0][0] == 1:
        res += 1
    if arr[1][0] == 1:
        res += 2
    if arr[2][0] == 1:
        res += 4
    if arr[3][0] == 1:
        res += 8
    print(res)
