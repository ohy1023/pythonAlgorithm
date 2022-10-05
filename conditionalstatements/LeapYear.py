year = int(input())


def isFourMul(year):
    if year % 4 == 0:
        return True
    return False

def isNotHundredMul(year):
    if year % 100 == 0:
        return False
    return True

def isFourHundredMul(year):
    if year % 400 == 0:
        return True
    return False


if (isFourMul(year) and isNotHundredMul(year) or isFourHundredMul(year)):
    print(1)
else:
    print(0)
