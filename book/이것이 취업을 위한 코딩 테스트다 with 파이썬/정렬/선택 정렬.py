def selection_sort():
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == "__main__":
    arr = [64, 6, 31, 14, 37, 25, 54, 100, 76, 42, 85]

    print(selection_sort())
