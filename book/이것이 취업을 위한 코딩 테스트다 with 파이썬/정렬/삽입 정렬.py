def insertion_sort():
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr


if __name__ == "__main__":
    arr = [64, 6, 31, 14, 37, 25, 54, 100, 76, 42, 85]

    print(insertion_sort())
