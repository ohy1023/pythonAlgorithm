def solve(a: list):
    N = int(input())
    for _ in range(N):
        a.append(int(input()))

    return sum(a)
