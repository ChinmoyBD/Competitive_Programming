def iceCreamParlor(m, arr):
    ice = len(arr)-1

    for i in range(ice):
        for j in range(i+1, ice+1):
            if arr[i] + arr[j] == m:
                return [i+1, j+1]


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        print(iceCreamParlor(m, arr))