import sys

input = sys.stdin.readline


def sol_split():
    cnt_one = 0
    cnt_zero = 0

    split_by_one = s.split('1')
    split_by_zero = s.split('0')

    for sbo in split_by_one:
        if sbo != '':
            cnt_one += 1

    for sbz in split_by_zero:
        if sbz != '':
            cnt_zero += 1

    return min(cnt_zero, cnt_one)


def sol_answer():
    count = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            count += 1
    return (count + 1) // 2


if __name__ == "__main__":
    s = input().strip()

    print(sol_split())
    print(sol_answer())
