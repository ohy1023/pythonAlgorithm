# pivot을 정한다.

def quick_sort(arr, start_idx, end_idx):
    lt = start_idx
    rt = end_idx
    pivot = arr[(lt + rt) // 2]

    while lt <= rt:
        while arr[lt] < pivot:
            lt += 1
        while arr[rt] > pivot:
            rt -= 1

        if lt <= rt:
            arr[lt], arr[rt] = arr[rt], arr[lt]
            lt += 1
            rt -= 1
    if start_idx < rt:
        quick_sort(arr, start_idx, rt)
    if end_idx > lt:
        quick_sort(arr, lt, end_idx)
    return arr

a = [20, 18, 5, 19, 40, 50, 5, 25]
print(quick_sort(a,0,len(a)-1))
