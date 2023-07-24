import sys

input = sys.stdin.readline


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        b = ''
        cnt = 1
        prev = s[0:i]
        for j in range(i, len(s), i):
            if prev == s[j:i + j]:
                cnt += 1
            else:
                b += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j + i]
                cnt = 1
        b += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(b))

    return answer


if __name__ == "__main__":
    print(solution("aabbaccc"))
