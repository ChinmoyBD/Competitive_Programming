def insertionSort2(n, arr):
    for i in range(1, n):
        item = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = item

        print(*arr)


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)