A = int (input())
B = int (input())

first = B % 10
second = (B % 100) // 10
third = B // 100

print(A * first, A * second, A * third, A * B,sep="\n")

