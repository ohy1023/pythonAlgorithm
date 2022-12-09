import sys


def solution(s1, s2):
    dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if s1[j - 1] == s2[i - 1] else max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s2)][len(s1)]


if __name__ == "__main__":
    seq1 = sys.stdin.readline().strip()
    seq2 = sys.stdin.readline().strip()

    print(solution(seq1, seq2))
