def reverseArray(a):
    _len = len(a)-1

    for i in range(len(a)//2):
        a[i], a[_len-i] = a[_len-i], a[i]

    return a


if __name__ == "__main__":
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(reverseArray(arr))