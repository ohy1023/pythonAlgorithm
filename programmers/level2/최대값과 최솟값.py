def solution(s):
    a = list(map(int, s.split()))
    answer = ('%d %d' % (min(a), max(a)))
    return answer
