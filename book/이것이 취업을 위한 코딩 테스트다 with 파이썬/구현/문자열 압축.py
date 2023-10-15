import sys

"""
이코테 level 2
문자열 압축 - 구현
"""


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        st = ''
        tmp_len = 1
        init_word = s[0:i]
        for j in range(i, len(s), i):
            if init_word == s[j:i + j]:
                tmp_len += 1
            else:
                st += str(tmp_len) + init_word if tmp_len >= 2 else init_word
                init_word = s[j:i + j]
                tmp_len = 1
        st += str(tmp_len) + init_word if tmp_len >= 2 else init_word

        answer = min(answer, len(st))
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    s = input().strip()
    print(solution(s))
