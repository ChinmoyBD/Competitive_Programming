def array_sum(arr):
    count = []

    for i in range(4):
        for j in range(4):
            su = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            '''
            su += sum(arr[i][j:3+j])
            su += arr[i+1][1+j]
            su += sum(arr[i+2][j:3+j])
            '''
            count.append(su)

    return max(count)


if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().strip().split())))

    print(array_sum(arr))