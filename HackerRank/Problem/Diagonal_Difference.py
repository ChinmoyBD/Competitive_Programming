

def diagonalDifference(arr):
    Lsum = 0
    Rsum = 0
    l = 0
    r = len(arr[0])-1
    for i in arr:
        Lsum += i[l]
        Rsum += i[r]
        l += 1
        r -= 1
    if Lsum > Rsum:
        return Lsum - Rsum
    else:
        return Rsum - Lsum



if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)