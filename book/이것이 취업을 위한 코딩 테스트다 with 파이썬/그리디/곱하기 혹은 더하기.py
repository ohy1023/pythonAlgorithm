"""
이코테 level.1
곱하기 혹은 더하기 - 그리디
"""

import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    number = input().strip()
    result = int(number[0])  # 첫 번째 숫자로 초기화

    for i in range(1, len(number)):
        num = int(number[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
