def solution(arr):
    for i in range(len(arr) - 1):
        minIdx = i
        for j in range(i+1,len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i],arr[minIdx] = arr[minIdx],arr[i]

    return arr

arr = [2,3,657,125,6,28,78]
print(solution(arr))


