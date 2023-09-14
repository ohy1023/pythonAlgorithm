import sys

"""
백준 14426 접두사 찾기 (실버 1) - 해시
https://www.acmicpc.net/problem/14426
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())  # 단어의 개수 n과 테스트 케이스의 개수 m 입력

    prefixes = {}  # 접두사를 저장할 딕셔너리 초기화
    for _ in range(n):
        word = input().strip()  # 단어 입력
        for i in range(1, len(word) + 1):
            prefix = word[:i]  # 현재 위치까지의 접두사
            prefixes[prefix] = True  # 딕셔너리에 접두사 저장

    count = 0  # 접두사를 찾은 횟수 초기화
    for _ in range(m):
        test_str = input().strip()  # 테스트할 문자열 입력
        if prefixes.get(test_str):  # 해당 문자열이 접두사 딕셔너리에 있는지 확인
            count += 1  # 접두사가 있을 경우 카운트 증가

    print(count)  # 결과 출력
