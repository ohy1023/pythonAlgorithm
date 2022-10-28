
def soultion(a):
    for i in range(9):
        hs1 = set()
        hs2 = set()
        for j in range(9):
            hs1.add(a[i][j])
            hs2.add(a[j][i])
        if len(hs1) != 9 or len(hs2) != 9:
            return False

    dx = [0, -1, 0, 1, 0, -1, 1, -1, 1]
    dy = [0, 0, 1, 0, -1, -1, -1, 1, 1]
    for i in range(1, 9, 3):
        hs3 = set()
        for j in range(1, 9, 3):
            for k in range(9):
                hs3.add(a[i + dx[k]][j + dy[k]])
            if len(hs3) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if soultion(a):
    print("YES")
else:
    print("NO")