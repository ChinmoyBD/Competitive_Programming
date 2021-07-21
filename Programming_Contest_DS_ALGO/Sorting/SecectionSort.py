def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(selectionSort([12, 3, 34, 23, 23, 324, 435]))