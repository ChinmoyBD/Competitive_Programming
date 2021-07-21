def hackerlandRadioTransmitters(x, k):
    x.sort()
    li = []
    d = 0

    while True:
        trans = x[0]
        l = len(x)
        for i in range(l):
            if x[0] + k >= x[i]:
                trans = x[i]
                d = i
            else:
                break
        next_i = d
        for i in range(d, l):
            if trans + k >= x[i]:
                next_i = i
            else:
                break
        li.append(trans)
        x = list(x[next_i+1:])

        if len(x) == 0:
            break

    return len(li)


if __name__ == "__main__":
    nk = input().split()
    k = int(nk[1])

    x = list(map(int, input().split()))

    print(hackerlandRadioTransmitters(x, k))