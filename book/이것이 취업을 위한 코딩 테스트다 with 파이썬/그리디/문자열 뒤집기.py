import sys

"""
이코테 level.1
문자열 뒤집기 - 그리디
"""


def sol_split():
    # 문자열을 '1'로 분할하고 빈 문자열을 제외한 후의 길이를 구함
    split_by_one = s.split('1')
    count_one = len(split_by_one) - split_by_one.count('')

    # 문자열을 '0'로 분할하고 빈 문자열을 제외한 후의 길이를 구함
    split_by_zero = s.split('0')
    count_zero = len(split_by_zero) - split_by_zero.count('')

    # 0과 1로 나눈 결과 중에서 더 적은 개수를 반환
    return min(count_zero, count_one)


def sol_answer():
    count = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            count += 1
    # 뒤집는 횟수를 세고, 2로 나누어 중복을 제외하여 반환
    return (count + 1) // 2


if __name__ == "__main__":
    input = sys.stdin.readline
    s = input().strip()

    print(sol_split())
    print(sol_answer())
