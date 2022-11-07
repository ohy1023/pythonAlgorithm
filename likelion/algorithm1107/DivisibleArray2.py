from queue import PriorityQueue

def solution(arr, divisor):
    answer = []
    que = PriorityQueue()
    for a in arr:
        if a % divisor == 0:
            que.put(a)
    if que.empty():
        return [-1]
    else:
        for _ in range(que.qsize()):
            answer.append(que.get())
        return answer
