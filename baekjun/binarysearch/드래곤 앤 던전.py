import sys

input = sys.stdin.readline


def clear_check(cur_atk, max_hp):
    cur_hp = max_hp
    for type, atk, hp in dungeons:
        if type == 1:  # 몬스터
            turn = hp // cur_atk if not hp % cur_atk else hp // cur_atk + 1  # A if not 조건 else B
            cur_hp -= atk * (turn - 1)
        else:  # 물약
            cur_atk += atk
            cur_hp += hp
            if cur_hp > max_hp:
                cur_hp = max_hp
        if cur_hp <= 0:  # 용사의 HP가 0이하라면 클리어 실패
            return False
    return True


if __name__ == "__main__":
    N, ATK = map(int, input().split())
    dungeons = []
    for _ in range(N):
        type, atk, hp = map(int, input().split())
        dungeons.append((type, atk, hp))

    lt, rt = 1, N * 1000000 * 1000000
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if clear_check(ATK, mid):
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1

    print(res)
