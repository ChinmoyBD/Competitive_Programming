def bubbleSort(arr):
    n = len(arr)
    for i in range(n):

        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubbleSort([5, 8, 6, 1, 7]))