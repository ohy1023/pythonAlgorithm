import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = input().strip()
    left = sum(int(x) for x in n[0:len(n) // 2])
    right = sum(int(x) for x in n[len(n) // 2:])

    if left == right:
        print("LUCKY")
    else:
        print("READY")
