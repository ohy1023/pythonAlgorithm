import sys
import string

"""
백준 16139 인간-컴퓨터 상호작용 (실버 1) - 누적 합
https://www.acmicpc.net/problem/16139
"""

input = sys.stdin.readline

if __name__ == "__main__":
    s = input().strip()
    q = int(input())
    questions = [(c, int(s), int(e)) for c, s, e in (input().split() for _ in range(q))]

    char_list = {}
    for char in string.ascii_lowercase:
        char_list[char] = [0]
        cnt = 0
        for i in range(len(s)):
            if s[i] == char:
                cnt += 1
            char_list[char].append(cnt)

    for question in questions:
        char, start, end = question[0], question[1], question[2],
        print(char_list[char][end + 1] - char_list[char][start])
