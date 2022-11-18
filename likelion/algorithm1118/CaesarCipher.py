def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        elif i.islower():
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    return answer


s = "abcdefghijklmnop"
n = 17
print(solution(s, n))
