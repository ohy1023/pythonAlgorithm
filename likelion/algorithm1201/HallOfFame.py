def solution(k, score):
    answer = []
    temp = []
    for i in score:
        if len(temp) < k:
            temp.append(i)
        elif i > min(temp):
            temp.remove(min(temp))
            temp.append(i)
        answer.append(min(temp))
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
