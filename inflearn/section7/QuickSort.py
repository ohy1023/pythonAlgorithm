def QSort(lt, rt):
    if lt < rt:
        pivot = arr[rt]
        pos = lt
        for i in range(lt, rt):
            if arr[i] < pivot:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        arr[pos], arr[rt] = arr[rt], arr[pos]
        QSort(lt, pos - 1)
        QSort(pos + 1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    QSort(0, 9)
    print(arr)
