def hackerlandRadioTransmitters(x, k):
    mi = min(x)
    ma = max(x)
    li = []
    for i in range(mi, ma + 1, 1):
        li.append(i)
    count = 0
    ex = x[0]
    while k < len(li) + 1:

        for j in range(len(x)):
            if k > len(li) - 1:
                k = len(li) - 2

            if ex < li[k]:
                if ex <= x[j]:
                    ex = x[j]
        for l in range(len(x)):
            if ex == x[l]:
                count += 1

        if li[k] > ex:
            for i in range(len(li)):
                if ex == li[i]:
                    k = k + ex + 1

        k += k

    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    print(result)
