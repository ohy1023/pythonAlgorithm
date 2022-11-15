def merge(arr1,arr2,arr3):
    list = arr1 + arr2 + arr3
    return list


def solution(arr):
    left = []
    mid = []
    right = []

    if len(arr) <= 1:
        return arr

    standard = arr[len(arr) // 2]

    for i in range(len(arr)):
        if arr[i] < standard:
            left.append(arr[i])
        elif arr[i] > standard:
            right.append(arr[i])
        else:
            mid.append(arr[i])

    return merge(solution(left),mid,solution(right))


print(solution([20, 18, 5, 19, 5, 25, 40, 50]))
