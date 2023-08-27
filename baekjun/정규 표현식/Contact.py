import re
import sys

input = sys.stdin.readline
if __name__ == "__main__":

    T = int(input())
    results = []

    for _ in range(T):
        sign = input().strip()
        p = re.compile('(100+1+|01)+')
        m = p.fullmatch(sign)
        if m:
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)
