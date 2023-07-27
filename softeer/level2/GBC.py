import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [0] * 101

    # Input 받을 때 바로 리스트에 저장하도록 변경
    heights_speeds_n = [map(int, input().split()) for _ in range(n)]
    heights_speeds_m = [map(int, input().split()) for _ in range(m)]

    # 이전 위치 기록 변수
    prev_pos = 1
    for height, speed in heights_speeds_n:
        # 현재 위치부터 높이만큼 반복하여 속도 기록
        for i in range(prev_pos, prev_pos + height):
            check[i] = speed
        prev_pos += height

    # 결과 값 변수
    res = 0
    prev_pos = 1
    for height, speed in heights_speeds_m:
        # 현재 위치부터 높이만큼 반복하여 속도 비교 및 결과 갱신
        for i in range(prev_pos, prev_pos + height):
            dif = speed - check[i]
            res = max(res, dif)
        prev_pos += height

    print(res)
