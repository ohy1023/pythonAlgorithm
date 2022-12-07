import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 heap으로 바꾸어 줌.
    while scoville[0] < K: # 최소값이 k 보다 작으면
        if len(scoville) == 1: # 더 이상 바꿀 수 없을 경우 추가
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))