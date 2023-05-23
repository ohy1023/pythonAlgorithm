from typing import List


# 나의 풀이 - 시간 초과
def solution_stack_time_limit(temperatures: List[int]) -> List[int]:
    for i in range(len(temperatures) - 1):
        stack.clear()
        temp = temperatures[i]
        stack.append(temp)
        for j in range(i + 1, len(temperatures)):
            if temp < temperatures[j]:
                res[i] = len(stack)
                break
            else:
                stack.append(temperatures[j])

    return res


# 스택 값 비교
def solution_stack(temperatures: List[int]) -> List[int]:
    for i, cur in enumerate(temperatures):
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            res[last] = i - last
        stack.append(i)
    return res


if __name__ == "__main__":
    T = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
    stack = []
    res = [0] * len(T)
    print(solution_stack(T))
    print(solution_stack_time_limit(T))
