def solution(s):
    answer = ''

    s = s.split(" ")

    for i in s:
        if i == "":
            answer += " "
            continue

        i = i.lower()

        if 48 <= ord(i[0]) <= 57:
            answer += i + " "
            continue
        else:
            memo = i[0]
            memo = memo.upper()
            i = memo + i[1:]
            answer += i + " "

    return answer[:-1]
