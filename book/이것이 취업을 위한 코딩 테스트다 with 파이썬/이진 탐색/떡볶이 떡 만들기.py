import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    rice_cakes = list(map(int, input().split()))

    # 절단기 길이로 이분 탐색 실시 
    lt, rt = 0, max(rice_cakes)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        # 절단기 길이가 mid일때 얻는 떡 (mid 보다 작으면 음수 가 되므로 제외 후 계산)
        tmp = sum([x - mid for x in rice_cakes if x > mid])

        # 얻은 떡이 목표값보다 작으면 절단기 길이를 줄임
        if tmp < m:
            rt = mid - 1
        # 얻은 떡이 목표값보다 크거나 같다면 절단기 길이를 느리고 결과값 저장
        else:
            res = mid
            lt = mid + 1

    print(res)
