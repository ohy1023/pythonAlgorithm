import sys
import heapq

input = sys.stdin.readline


def solution(food_times, k):
    answer = -1
    hq = []

    for idx, food_time in enumerate(food_times):
        heapq.heappush(hq, (food_time, idx + 1))

    rest_cnt = len(food_times)
    previous = 0

    while hq:
        t = (hq[0][0] - previous) * rest_cnt

        if k >= t:
            k -= t
            previous, _ = heapq.heappop(hq)
            rest_cnt -= 1
        else:
            idx = k % rest_cnt
            hq.sort(key=lambda x: x[1])
            answer = hq[idx][1]
            break

    return answer


if __name__ == "__main__":
    print(solution([3, 1, 2], 5))
