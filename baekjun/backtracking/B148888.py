def DFS(depth, total, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == N:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return
    else:
        if plus:
            DFS(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
        if minus:
            DFS(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
        if multiply:
            DFS(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
        if divide:
            DFS(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    calculates = list(map(int, input().split()))
    max_num = -2147000000
    min_num = 2147000000
    DFS(1, nums[0], calculates[0], calculates[1], calculates[2], calculates[3])
    print(max_num)
    print(min_num)
