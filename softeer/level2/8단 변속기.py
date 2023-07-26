import sys

input = sys.stdin.readline

gear_steps = list(map(int, input().split()))

if all(i == gear_steps[i - 1] for i in range(1, 9)):
    print("ascending")
elif all(i == gear_steps[-i] for i in range(1, 9)):
    print("descending")
else:
    print("mixed")