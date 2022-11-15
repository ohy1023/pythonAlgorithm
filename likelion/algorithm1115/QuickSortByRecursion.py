def merge(arr1,arr2,arr3):
    list = arr1 + arr2 + arr3
    return list


def solution(arr):
    left = []
    mid = []
    right = []

    if len(arr) <= 1:
        return arr

    center = len(arr) // 2
    standard = arr[center]

    mid.append(standard)

    lt = center - 1
    rt = center + 1
    while lt != -1:
        if arr[lt] < arr[center]:
            left.append(arr[lt])
        elif arr[lt] > arr[center]:
            right.append(arr[lt])
        else:
            mid.append(arr[lt])
        lt -= 1

    while rt != len(arr):
        if arr[rt] < arr[center]:
            left.append(arr[rt])
        elif arr[rt] > arr[center]:
            right.append(arr[rt])
        else:
            mid.append(arr[rt])
        rt += 1

    return merge(solution(left),mid,solution(right))


print(solution([20, 18, 5, 19, 5, 25, 40, 50]))
