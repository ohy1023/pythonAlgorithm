def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


num = int(input())
arr = [0] * num
for i in range(num):
    arr[i] = int(input())
print(bubbleSort(arr))