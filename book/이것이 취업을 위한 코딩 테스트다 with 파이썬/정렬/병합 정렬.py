def merge_sort_ver_01(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_side = merge_sort_ver_01(arr[:mid])
    right_side = merge_sort_ver_01(arr[mid:])

    answer = []
    l = h = 0
    while l < len(left_side) and h < len(right_side):
        if left_side[l] < right_side[h]:
            answer.append(left_side[l])
            l += 1
        else:
            answer.append(right_side[h])
            h += 1

    answer += left_side[l:]
    answer += right_side[h:]
    return answer


def merge_sort_ver_02(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


if __name__ == "__main__":
    nums = [64, 6, 31, 14, 100, 37, 25, 54, 100, 76, 42, 85, 6]

    print(merge_sort_ver_01(nums))
    merge_sort_ver_02(nums)
    print(nums)
