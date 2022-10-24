# 배열 슬라이싱 사용
def solution(arr, commands):
    answer = []
    for i in range(len(commands)):
        result = sorted(arr[commands[i][0] - 1:commands[i][1]])
        answer.append(result[commands[i][2] - 1])

    return answer


from queue import PriorityQueue

# 우선순위 큐 사용
def kthNum(arr, command):
    start = command[0] - 1
    end = command[1]
    kth = command[2]
    rst = 0

    que = PriorityQueue()
    for i in range(start, end):
        que.put(arr[i])

    for _ in range(kth):
        rst = que.get()
    return rst


def solution2(arr, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(kthNum(arr, commands[i]))
    return answer


arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution2(arr, commands))
