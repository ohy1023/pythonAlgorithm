def solution(s):
    answer = []
    cnt_binary = 0
    cnt_zero_sum = 0
    while s != "1":
        cnt_zero = 0
        for i in s:
            if i == "0":
                cnt_zero += 1

        s = bin(len(s) - cnt_zero)[2:]
        cnt_binary += 1
    answer.append(cnt_binary)
    answer.append(cnt_zero_sum)

    return answer


print(solution("01110"))
