def solution_stack(s: str) -> bool:
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


if __name__ == "__main__":
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    print(solution_stack("()[]{}"))
