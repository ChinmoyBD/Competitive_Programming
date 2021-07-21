def birthday(s, d, m):
    count = 0
    for i in range(0, len(s) - m + 1, 1):
        _sum = 0
        for j in range(0, m, 1):
            _sum += s[i + j]
        if _sum == d:
            count += 1

    return count


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
