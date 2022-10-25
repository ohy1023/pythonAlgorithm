HH, MM = map(int,input().split())

if MM < 45:
    if HH == 0:
        HH = 23
    else:
        HH -= 1
    MM = 60 - (45 - MM)
    print(HH, MM, sep=' ')
else:
    MM -= 45
    print(HH, MM, sep=' ')
