import sys

input = sys.stdin.readline


def solution_stack(s: str) -> bool:
    stack = []

    for char in s:
        if char in ['(', '[']:
            stack.append(char)
        elif char in [')', ']']:
            if not stack or table[char] != stack.pop():
                return False
    return len(stack) == 0


if __name__ == "__main__":
    table = {
        ')': '(',
        ']': '['
    }
    while True:
        statement = input().rstrip()
        if statement == '.':
            break
        print("yes" if solution_stack(statement) else "no")
