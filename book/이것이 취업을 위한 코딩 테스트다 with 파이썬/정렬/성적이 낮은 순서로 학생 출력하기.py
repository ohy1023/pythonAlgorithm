import sys

input = sys.stdin.readline

n = int(input())
students = sorted([(name, int(score)) for name, score in (input().split() for _ in range(n))], key=lambda x: x[1])

for student in students:
    print(student[0], end=' ')
