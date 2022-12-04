def solution(v, s):
    global answer
    if v >= answer:
        return
    if s > m:
        return
    elif s == m:
        if answer > v:
            answer = v
        return
    else:
        for t in type:
            solution(v + 1, s + t)


if __name__ == "__main__":
    n = int(input())
    type = list(map(int, input().split()))
    type.sort(reverse=True)
    m = int(input())
    answer = 2147000000
    solution(0, 0)
    print(answer)
