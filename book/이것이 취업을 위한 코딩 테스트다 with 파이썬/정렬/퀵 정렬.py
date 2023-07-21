def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


if __name__ == "__main__":
    arr = [64, 6, 31, 14, 37, 25, 54, 100, 76, 42, 85]

    print(quick_sort(arr))
