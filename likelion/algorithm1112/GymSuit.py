# 내 풀이
def solution(n, lost, reserve):
    answer = 0
    count = [1] * (n +2)
    for i in lost:
        count[i] -= 1
    for j in reserve:
        count[j] += 1
    print(count)
    for k in range(1, n + 2):
        if count[k] == 2:
            if count[k - 1] == 0:
                count[k] -= 1
                count[k - 1] += 1
            elif count[k + 1] == 0:
                count[k] -= 1
                count[k + 1] += 1
    for l in range(1,n+1):
        if count[l] >= 1:
            answer += 1
    return answer

# 프로그래머스 풀이
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    print(_reserve)
    _lost = [l for l in lost if l not in reserve]
    print(_lost)
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


print(solution2(7, [1,3,5], [3,4,7]))
