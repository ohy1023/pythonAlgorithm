import sys
from itertools import combinations

"""
백준 1759 암호 만들기 (골드 5) - 백트래킹
https://www.acmicpc.net/problem/1759
"""

input = sys.stdin.readline

if __name__ == "__main__":
    vowels = ['a', 'e', 'i', 'o', 'u']
    l, c = map(int, input().split())
    alps = sorted(list(map(str, input().split())))

    for password in combinations(alps, l):
        cnt = 0
        for i in password:
            if i in vowels:
                cnt += 1

        if 1 <= cnt <= l - 2:
            print("".join(password))
