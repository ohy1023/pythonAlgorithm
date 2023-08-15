import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    warehouses = list(map(int, input().split()))
    dy = [0] * n

    # [1, 3, 1, 5]
    # 각 날에 최대값을 저장
    dy[0] = warehouses[0]  # 첫째 날은 경우의 수가 하나 밖에 없으므로 첫번째 값 저장
    dy[1] = max(warehouses[0], warehouses[1])  # 둘째 날은 첫번째 창고 와 두번째 창고는 더 큰 값을 저장 - 연달아 털 수 없으므로
    for i in range(2, n):
        dy[i] = max(dy[i - 2] + warehouses[i], dy[i - 1])

    print(dy[n - 1])
