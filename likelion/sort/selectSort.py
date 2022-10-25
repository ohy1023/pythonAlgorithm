def selectSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i + 1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr


num=int(input())
arr=[0]*num
for k in range(num):
    arr[k]=int(input())

selectSort(arr)
for p in arr:
    print(p)



