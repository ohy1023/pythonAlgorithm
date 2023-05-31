import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    assignments = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1])
    ch = [0] * 1000
    answer = 0
    for due, score in assignments:
        i = due
        while i > 0 and ch[i] == 1:
            i -= 1
        if i != 0:
            ch[i] = 1
            answer += score

    print(answer)
