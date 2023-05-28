def solution(clothes):
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    ans = 1
    for type in hash_map:
        ans *= (hash_map[type] + 1)

    return ans - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))