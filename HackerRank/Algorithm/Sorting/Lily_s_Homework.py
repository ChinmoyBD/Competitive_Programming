def lilysHomework(n, arr):
    count = 0
    for i in range(n):
        b_l = False
        s1 = arr[i]

        for j in range(i+1, n):
            if s1 > arr[j]:
                s1 = arr[j]
                index = j
                b_l = True
        if b_l is True:
            arr[i], arr[index] = arr[index], arr[i]
            count += 1

    return count


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().split()))

    print(lilysHomework(n, arr))