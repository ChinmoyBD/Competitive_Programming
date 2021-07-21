def binary_search(arr, i):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if brr[mid] == i:
            return True
        if brr[mid] < i:
            left = mid + 1
        else:
            right = mid - 1

    return False


def missingNumbers(arr, brr):
    arr.sort()
    missing = []

    for i in brr:
        if binary_search(arr, i) is False:
            missing.append(i)

    return missing


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().split()))

    m = int(input())

    brr = list(map(int, input().split()))

    print(missingNumbers(arr, brr))