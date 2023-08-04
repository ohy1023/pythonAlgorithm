import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    money = int(input())
    days = list(map(int, input().split()))

    jun_money, sung_money = money, money
    jun_res, sung_res = 0, 0
    buy_cnt = 0
    up, down = 0, 0
    for i in range(len(days)):
        if jun_money >= days[i]:
            jun_res += days[-1] * (jun_money // days[i])
            jun_money %= days[i]

    if jun_money != 0:
        jun_res += jun_money

    for j in range(1, len(days)):
        if days[j] > days[j - 1]:
            up += 1
            down = 0
        elif days[j] < days[j - 1]:
            down += 1
            up = 0
        else:
            up = 0
            down = 0
        if down >= 3:
            if sung_money >= days[j]:
                buy_cnt += (sung_money // days[j])
                sung_money %= days[j]

        if up >= 3:
            sung_money += days[j] * buy_cnt
            buy_cnt = 0

    sung_res += (days[-1] * buy_cnt) + sung_money

    if jun_res > sung_res:
        print("BNP")
    elif jun_res < sung_res:
        print("TIMING")
    else:
        print("SAMESAME")