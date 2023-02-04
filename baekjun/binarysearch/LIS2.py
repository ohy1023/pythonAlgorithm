import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
res = [0]

for s in sequence:
    if res[-1] < s:
        res.append(s)
    else:
        lt = 1
        rt = len(res)

        while lt < rt:
            mid = (lt + rt) // 2
            if res[mid] < s:
                lt = mid + 1
            else:
                rt = mid
        res[rt] = s
print(len(res) - 1)
