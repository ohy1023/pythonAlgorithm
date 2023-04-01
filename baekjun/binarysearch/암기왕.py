import sys

input = sys.stdin.readline


def binary_search(num, book1):
    lt = 0
    rt = len(book1) - 1

    while lt <= rt:
        mid = (lt + rt) // 2
        if book1[mid] == num:
            return 1
        elif book1[mid] < num:
            lt = mid + 1
        else:
            rt = mid - 1
    return 0


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        book1 = sorted(list(map(int, input().split())))
        m = int(input())
        book2 = list(map(int, input().split()))
        for num in book2:
            print(binary_search(num, book1))
