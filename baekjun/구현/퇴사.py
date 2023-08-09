import sys


def brute_force(day, reward):
    global res

    if day == n:  # 퇴사일
        if res < reward:
            res = reward
        return
    if day > n:
        return  # 퇴사일 초과하여 불가

    brute_force(day + schedules[day][0], reward + schedules[day][1])
    brute_force(day + 1, reward)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    schedules = [tuple(map(int, input().split())) for _ in range(n)]

    res = 0
    brute_force(0, 0)
    print(res)
