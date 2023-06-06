from collections import Counter


def str_split(s, arr):
    for i in range(len(s) - 1):
        if s[i:i + 2].isalpha():
            arr.append(s[i:i + 2].lower())


def solution(str1, str2):
    str1_list = []
    str2_list = []
    str_split(str1, str1_list)
    str_split(str2, str2_list)

    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)

    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)


if __name__ == "__main__":
    print(solution("handshake", "shake hands"))
