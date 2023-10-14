import sys
import re

"""
이코테 level.1
문자열 재정렬 - 구현
"""


# 선형 탐색을 사용하여 문자와 숫자를 분리하고 정렬하는 함수
def sol_linear_search(S):
    strs = []  # 문자를 저장할 리스트
    nums = []  # 숫자를 저장할 리스트

    # 주어진 문자열 S를 문자와 숫자로 분리
    for string in S:
        if string.isalpha():  # 문자인 경우
            strs.append(string)  # 문자 리스트에 추가
        else:
            nums.append(int(string))  # 숫자 리스트에 추가

    strs.sort()  # 문자열 정렬

    # 문자열과 숫자를 조합하여 결과 문자열 생성
    res = ''.join(strs) + ('' if sum(nums) == 0 else str(sum(nums)))

    print(res)  # 결과 출력


# 정규 표현식을 사용하여 문자와 숫자를 분리하고 정렬하는 함수
def sol_re(S):
    # 정규 표현식을 사용하여 숫자와 문자를 분리
    char_matches = re.findall(r'[a-zA-Z]', S)  # 문자 추출
    num_matches = re.findall(r'\d', S)  # 숫자 추출

    char_matches.sort()  # 문자열 정렬

    # 분리된 숫자를 합하여 문자열을 생성
    num_str = str(sum(map(int, num_matches))) if num_matches else ""

    # 정렬된 문자와 합쳐진 숫자를 조합하여 결과 문자열 생성
    res = ''.join(char_matches) + num_str

    print(res)  # 결과 출력


if __name__ == "__main__":
    input = sys.stdin.readline
    S = input().strip()

    # 두 가지 버전의 함수를 호출하여 실행
    sol_linear_search(S)  # 선형 탐색을 사용하는 함수
    sol_re(S)  # 정규 표현식을 사용하는 함수
