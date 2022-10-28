def solution(phone_book):
    hs = set()
    for a in phone_book:
        hs.add(a)
    for a in phone_book:
        for i in range(1,len(a)):
            if a[0:i] in hs:
                return False
    return True