def dilation(li, item):
    n = len(li)

    for i in range(n):
        if li[i] == item:
            index = i
            break
    for i in range(index, n-1):
        li[i] = li[i+1]

    return li[:-1]


if __name__ == "__main__":
    li = list(map(int, input().split()))
    n = int(input())
    dilation(li, n)
    print(li)
