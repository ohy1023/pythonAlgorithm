import sys

input = sys.stdin.readline

if __name__ == "__main__":
    strings = input().strip()
    strs = []
    nums = []
    for string in strings:
        if string.isalpha():
            strs.append(string)
        else:
            nums.append(int(string))

    strs.sort()

    res = ''.join(strs) + ('' if sum(nums) == 0 else str(sum(nums)))

    print(res)
