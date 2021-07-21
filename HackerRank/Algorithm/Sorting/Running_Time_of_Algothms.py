def runningTime(arr):
    n = len(arr)
    time = 0

    for i in range(1, n):
        item = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j-1

            time += 1

        arr[j+1] = item
    return time


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().split()))

    print(runningTime(arr))
