def equalStacks(h1, h2, h3):
    s1, s2, s3 = map(sum, (h1, h2, h3))

    while h1 and h2 and h3:
        m = min(s1, s2, s3)
        while s1 > m: s1 -= h1.pop(0)
        while s2 > m: s2 -= h2.pop(0)
        while s3 > m: s3 -= h3.pop(0)
        if s1 == s2 == s3:
            return s3
    return 0


if __name__ == '__main__':
    n1, n2, n3 = map(int, input().split())

    h1 = list(map(int, input().split()))
    h2 = list(map(int, input().split()))
    h3 = list(map(int, input().split()))

    print(equalStacks(h1, h2, h3))