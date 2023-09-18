import sys

"""
백준 2493 탑 (골드 5) - 스택
https://www.acmicpc.net/problem/2493
"""

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())  # 탑의 개수 입력
    tops = list(map(int, input().split()))  # 탑의 높이 정보 입력
    tops.insert(0, 0)  # 인덱스를 1부터 시작하기 위해 0 추가

    res = [0] * (n + 1)  # 수신한 탑의 번호를 저장할 리스트 초기화
    stack = []  # 스택 초기화

    for i in range(1, n + 1):
        while stack:
            if tops[i] > stack[-1][0]:  # 현재 탑의 높이가 스택의 맨 위 탑보다 높을 경우
                stack.pop()  # 스택에서 탑을 제거 (수신할 수 없음)
            else:
                res[i] = stack[-1][1]  # 스택의 맨 위 탑이 수신하는 탑의 번호
                break
        stack.append((tops[i], i))  # 현재 탑을 스택에 추가

    print(*res[1::])  # 결과 출력 (1부터 끝까지)
