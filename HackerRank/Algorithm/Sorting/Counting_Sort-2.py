def countingSort(arr):
    count = [0] * 101
    sort_ = []

    for i in arr:
        count[i] += 1

    for index, value in enumerate(count):
        if value > 0:
            sort_.extend([index] * value)

    return sort_


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().split()))

    print(countingSort(arr))
