def solution(input_string):
    count = {}
    answer_list = []
    for idx, alpha in enumerate(input_string):
        if alpha not in count:
            count[alpha] = [idx]
        else:
            count[alpha].append(idx)
    for key, value in count.items():
        if len(value) >= 2:
            for i in range(len(value) - 1):
                if abs(value[i] - value[i + 1]) > 1:
                    answer_list.append(key)
                    break
    if len(answer_list) == 0:
        answer = "N"
    else:
        answer = ''.join(sorted(answer_list))

    return answer


if __name__ == "__main__":
    print(solution(input()))
