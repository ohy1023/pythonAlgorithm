import sys

"""
백준 1541 잃어버린 괄호 (실버 2) - 그리디
https://www.acmicpc.net/problem/1541
"""

if __name__ == "__main__":
    input = sys.stdin.readline

    # 입력 받은 수식을 '-' 기호를 기준으로 분할
    split_nums = input().strip().split("-")

    nums = []
    # 분할된 숫자들을 처리하여 합산하여 nums 리스트에 저장
    for split_num in split_nums:
        split = [int(x) for x in split_num.split("+")]
        nums.append(sum(split))

    n = nums[0]
    # 뺄셈을 수행하여 결과 계산
    for i in range(1, len(nums)):
        n -= nums[i]

    # 최종 결과 출력
    print(n)
