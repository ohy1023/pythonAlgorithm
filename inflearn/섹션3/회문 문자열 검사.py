N = int(input())

for i in range(N):
    word = input()
    word = word.upper()
    if word == word[::-1]:
        print("#%d %s"%(i+1,"YES"))
    else:
        print("#%d %s"%(i+1,"NO"))
