from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        answer += 1

    if people:
        answer += 1

    return answer
