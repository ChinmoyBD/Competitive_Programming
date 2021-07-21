def binary_search(L, X):
    left, right = 0, len(L)-1

    while left <= right:
        mid = (left + right) // 2
        if L[mid] == X:
            return mid
        if L[mid] < X:
            left = mid + 1
        else:
            right = mid - 1
    return -1
if __name__ =="__main__":
    li = [1, 4, 6, 7, 10, 19, 22, 23, 30, 35, 39, 46, 49, 50, 52, 55, 61, 67, 70, 71]
    call = binary_search(li, 70)
    print(call)