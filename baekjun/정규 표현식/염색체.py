import sys
import re

"""
백준 9342 염색체 (실버 3) - 정규 표현식
https://www.acmicpc.net/problem/9342
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    pattern = re.compile("^[A-F]?A+F+C+[A-F]?$")
    for _ in range(n):
        input_value = input().strip()

        if pattern.match(input_value):
            print("Infected!")
        else:
            print("Good")
