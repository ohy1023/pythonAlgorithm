def solution(n):
    dy = [0] * (n + 1)
    dy[0] = 0
    dy[1] = 1
    for i in range(2, n + 1):
        dy[i] = dy[i - 1] + dy[i - 2]
    answer = dy[n]
    return answer % 1234567


print(solution(12421))
