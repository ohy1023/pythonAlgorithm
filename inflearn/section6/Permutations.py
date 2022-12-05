from itertools import permutations

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [x for x in range(1, n + 1)]

    answers = list(map(list, permutations(a, m)))
    for answer in answers:
        for a in answer:
            print(a, end=" ")
        print()
    print(len(answer))
