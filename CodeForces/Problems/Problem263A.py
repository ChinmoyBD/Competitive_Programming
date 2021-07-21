def beautiful_matrix(li):
    r = c = 2
    for i in range(5):
        for j in range(5):
            if li[i][j] == 1:
                break
        if li[i][j] == 1:
            break
    if r < i:
        r, i = i, r
    if c < j:
        c, j = j, c

    print((r-i)+(c-j))


if __name__ == "__main__":
    arr = []
    for _ in range(5):
        li = list(map(int, input().split()))
        arr.append(li)

    beautiful_matrix(arr)
