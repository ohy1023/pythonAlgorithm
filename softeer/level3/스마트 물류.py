import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = [string for string in input().strip()]
    ch = [False] * n
    res = 0
    for i in range(n):
        if arr[i] == 'P':
            for j in range(-k, k + 1):
                if 0 <= i + j < n and arr[i + j] == 'H' and not ch[i + j]:
                    ch[i + j] = True
                    res += 1
                    break

    print(res)
