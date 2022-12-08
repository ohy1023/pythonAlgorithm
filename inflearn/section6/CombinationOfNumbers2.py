import itertools as lt

if __name__ == "__main__":
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    for i in lt.combinations(numbers, k):
        if sum(i) % m == 0:
            cnt += 1
    print(cnt)
