from collections import Counter, defaultdict


# 풀이 1 - 해시 테이블 (32ms)
def solution_hash_table(J: str, S: str) -> int:
    hash_map = {}
    count = 0

    for char in S:
        if char not in hash_map:
            hash_map[char] = 1
        else:
            hash_map[char] += 1

    for char in J:
        count += hash_map[char]

    return count


# 풀이 2 - defaultdict (28ms)
def solution_defaultdict(J: str, S: str) -> int:
    hash_map = defaultdict(int)
    count = 0

    for char in S:
        hash_map[char] += 1

    for char in J:
        count += hash_map[char]

    return count


# 풀이 3 - Counter (32ms)
def solution_counter(J: str, S: str) -> int:
    hash_map = Counter(S)
    count = 0

    for char in J:
        count += hash_map[char]

    return count


# 풀이 4 - 파이썬 다운 방식 (28ms)
def solution_list_comprehension(J: str, S: str) -> int:
    return sum(s in J for s in S)


if __name__ == "__main__":
    print(solution_hash_table("aA", "aAAbbbb"))
    print(solution_defaultdict("aA", "aAAbbbb"))
    print(solution_counter("aA", "aAAbbbb"))
    print(solution_list_comprehension("aA", "aAAbbbb"))
