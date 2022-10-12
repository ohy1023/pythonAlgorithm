import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
print(min(a),max(a),sep=" ")
