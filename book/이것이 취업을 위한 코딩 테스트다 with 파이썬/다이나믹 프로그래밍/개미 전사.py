import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    warehouses = list(map(int, input().split()))
    dy = [0] * 101

    # 최대값을 누적하여 저장
    dy[1] = warehouses[0]  # 경우의 수가 하나밖에 없으므로 첫 번째 값 저장
    dy[2] = max(warehouses[0], warehouses[1])  # 연달아 털 수 없으므로 첫 번째 창고 와 두 번째 창고에서 더 큰 값을 저장
    for i in range(3, n + 1):
        dy[i] = max(dy[i - 2] + warehouses[i - 1],
                    dy[i - 1])  # 한 칸 건너 띄고 현재 창고를 털었을 때의 값과 바로 전의 창고를 털었을 때의 값을 비교 후 큰 값을 저장

    print(dy[n])
