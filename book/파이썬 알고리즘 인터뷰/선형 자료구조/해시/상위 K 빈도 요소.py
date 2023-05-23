import heapq
from typing import List
from collections import Counter, defaultdict


def solution_hash(nums: List[int], k: int) -> List[int]:
    hash_map = defaultdict(int)
    result = []

    for num in nums:
        hash_map[num] += 1

    for key, value in hash_map.items():
        if value >= k:
            result.append(key)

    return result


def solution_counter(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    result = []

    for c in counter:
        heapq.heappush(result, (-counter[c], c))

    top_k = list()
    for _ in range(k):
        top_k.append(heapq.heappop(result)[1])

    return top_k


def solution_only_python(nums: List[int], k: int) -> List[int]:
    return list(list(zip(*Counter(nums).most_common(k)))[0])


if __name__ == "__main__":
    print(solution_hash([1, 1, 1, 2, 2, 3], 2))
    print(solution_counter([1, 1, 1, 2, 2, 3], 2))
    print(solution_only_python([1, 1, 1, 2, 2, 3], 2))
