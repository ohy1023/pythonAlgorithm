import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    stocks = sorted(list(map(int, input().split())))
    m = int(input())
    orders = list(map(int, input().split()))

    for order in orders:
        lt, rt = 0, n - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if stocks[mid] == order:
                print("yes", end=' ')
                break
            elif stocks[mid] > order:
                rt = mid - 1
            else:
                lt = mid + 1
        else:
            print("no", end=' ')
