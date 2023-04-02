import sys

input = sys.stdin.readline


def binary_search(k):
    lt, rt = 0, len(n_list) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if n_list[mid] == k:
            return 1
        elif n_list[mid] < k:
            lt = mid + 1
        else:
            rt = mid - 1
    return 0


if __name__ == "__main__":
    n = int(input())
    n_list = sorted(list(map(int, input().split())))
    m = int(input())
    m_list = list(map(int, input().split()))
    for num in m_list:
        print(binary_search(num))
