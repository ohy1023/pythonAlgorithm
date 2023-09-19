"""
이코테 level.1
모험가 길드 - 그리디
"""

import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())  # 모험가 수 입력
    fears = sorted(list(map(int, input().split())))  # 공포도를 오름차순으로 정렬

    res = 0  # 그룹 수 초기화
    cnt = 0  # 현재 그룹에 포함된 모험가 수 초기화

    for fear in fears:
        cnt += 1  # 모험가를 현재 그룹에 포함시킴
        if cnt >= fear:  # 현재 그룹에 포함된 모험가 수가 그의 공포도 이상이면 그룹을 결성
            res += 1  # 그룹 수 증가
            cnt = 0  # 현재 그룹에 포함된 모험가 수 초기화

    print(res)  # 결과 출력