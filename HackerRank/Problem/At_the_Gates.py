def pas(arr, k, n):
    for _ in range(1, k + 1):
        if arr[-1] == 'H':
            for i in range(len(arr) - 1):
                if arr[i] == 'H':
                    arr[i] = 'T'
                else:
                    arr[i] = 'H'
        n -= 1
        arr = arr[:n]

    return arr.count('H')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        arr = list(input().rstrip().split())

        print(pas(arr, k, n))
