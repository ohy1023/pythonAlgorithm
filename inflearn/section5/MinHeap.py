from queue import PriorityQueue

hp = PriorityQueue()
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(hp.get())
    else:
        hp.put(n)
