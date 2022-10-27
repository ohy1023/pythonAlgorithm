def solution(participant, completion):
    a = dict()
    for p in participant:
        a[p]=a.get(p,0)+1
    for c in completion:
        a[c] = a.get(c) -1
    for i in a:
        if a.get(i)==1:
            answer = i
            return answer
    return ""

