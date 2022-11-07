def sumAll(x):
    sumNum = 0
    while x > 0:
        sumNum += x % 10
        x //= 10
    return sumNum

def solution(x):
    if x % sumAll(x) == 0:
        answer = True
    else:
        answer = False
    print(answer)
    return answer

solution(182)