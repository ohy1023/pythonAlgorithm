import sys

input = sys.stdin.readline

nums = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1110010',
    '8': '1111111',
    '9': '1111011',
    ' ': '0000000'
}


def fill_with_spaces(s, n):
    spaces_to_add = max(0, n - len(s))
    return ' ' * spaces_to_add + s


def count_diff(a, b):
    return sum(nums[a[i]][j] != nums[b[i]][j] for i in range(5) for j in range(7))


t = int(input())
for _ in range(t):
    a, b = map(str, input().split())

    print(count_diff(fill_with_spaces(a, 5), fill_with_spaces(b, 5)))
