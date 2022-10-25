def solution(s):
    while (s.find("()") >= 0):
        s = s.replace("()","")
    return len(s) == 0


