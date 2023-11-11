"""
프로그래머스 소수 찾기 (Level.2) - 완전 탐색
https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
"""

from itertools import permutations


# 소수 판별 함수
def check_prime(nums):
    # 결과 값
    answer = 0

    # 에라토스테네스의 체
    max_num = max(nums)
    arr = [True] * (max_num + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, max_num + 1, i):
                arr[j] = False

    # 소수 개수 구하기
    for num in nums:
        if arr[num]:
            answer += 1

    return answer


def solution(numbers):
    # 경우의 수 찾기
    nums = []

    # 한자리 경우
    for n in numbers:
        if int(n) not in nums:
            nums.append(int(n))

    # 두자리 이상인 경우
    for i in range(2, len(numbers) + 1):
        for c in list(permutations([n for n in numbers], i)):
            number = ""
            for x in c:
                number += x

            if int(number) not in nums:
                nums.append(int(number))

    return check_prime(nums)


if __name__ == "__main__":
    print(solution("17"))
