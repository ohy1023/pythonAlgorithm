import sys

"""
백준 9251 LCS (골드 5) - DP
https://www.acmicpc.net/problem/9251
"""

if __name__ == "__main__":
    input = sys.stdin.readline

    # 두 문자열 입력
    word1 = input().strip()
    word2 = input().strip()

    h, w = len(word1), len(word2)

    # DP 테이블 초기화
    dp = [[0] * (w + 1) for _ in range(h + 1)]

    # LCS 계산
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if word1[i - 1] == word2[j - 1]:  # 문자가 같을 경우
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 문자가 다를 경우
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 최장 공통 부분 수열의 길이 출력
    print(dp[-1][-1])
