import sys

N,X =map(int,sys.stdin.readline().split())
A = map(int,sys.stdin.readline().split())
for x in A:
    if X > x:
        print(x,end=" ")