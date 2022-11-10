def solution(arr):
    stack = []
    stack.append(arr[0])
    for i in arr[1:]:
        top = stack[-1]
        if top != i:
            stack.append(i)
    return stack

arr = [1,1,3,3,0,1,1]

print(solution(arr))