def pairs(k, arr):
    l_arr = len(arr)
    value, count = 0, 0

    for i in range(l_arr):
        for j in range(i+1, l_arr):
            value = arr[i] - arr[j]
            if value < 0:
                value = value - (value*2)
            if value == k:
                count += 1
    return count


if __name__ == "__main__":
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    print(pairs(k, arr))