def solution(answers):
    firstStudent = [1,2,3,4,5]
    secondStudent = [2,1,2,3,2,4,2,5]
    thirdStudent = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == firstStudent[idx%len(firstStudent)]:
            score[0] += 1
        if answer == secondStudent[idx%len(secondStudent)]:
            score[1] += 1
        if answer == thirdStudent[idx%len(thirdStudent)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result