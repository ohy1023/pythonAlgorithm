T = int(input())
for i in range(T):
    sum = 0
    score = 0
    result = input()
    for x in result:
        if x == "O":
            sum += 1
            score += sum
        else:
            sum = 0

    print(score)
