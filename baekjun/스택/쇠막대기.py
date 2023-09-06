import sys

"""
백준 10799 쇠막대기 (실버 2) - 스택
https://www.acmicpc.net/problem/10799
"""


def solution(string):
    cnt = 0  # 잘려진 쇠막대기 조각의 총 개수 초기화
    stack = []  # 스택 초기화

    for i in range(len(string)):
        if string[i] == '(':  # 여는 괄호인 경우 스택에 추가
            stack.append(string[i])
        else:  # 닫는 괄호인 경우
            stack.pop()  # 스택에서 맨 위의 여는 괄호 제거
            if string[i - 1] == '(':  # 바로 이전 문자가 여는 괄호인 경우
                cnt += len(stack)  # 현재 스택의 길이만큼 조각 추가 (레이저로 잘려난 조각)
            else:  # 바로 이전 문자가 닫는 괄호인 경우
                cnt += 1  # 새로운 쇠막대기의 끝 부분 조각 추가

    return cnt  # 결과 반환


if __name__ == "__main__":
    input = sys.stdin.readline

    str = input().strip()  # 입력 문자열 받아옴
    print(solution(str))  # 결과 출력
