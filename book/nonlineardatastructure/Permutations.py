import itertools

# 재귀를 이용한 순열
def permute(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

def solution(nums):
    return list(map(list,itertools.permutations([1,2,3])))

if __name__=="__main__":
    print(solution([1,2,3]))
    print(list(map(list,solution([1,2,3]))))

