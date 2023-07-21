def counting_sort():
    count = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            answer.append(i)

    return answer


if __name__ == "__main__":
    arr = [64, 6, 31, 14, 100, 37, 25, 54, 100, 76, 42, 85, 6]
    answer = []

    print(counting_sort())
