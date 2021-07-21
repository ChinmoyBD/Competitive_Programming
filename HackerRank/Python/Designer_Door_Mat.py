
if __name__ == "__main__":
    n, m = map(int, input().split())
    _sum = 0
    ra = (n // 2)**2
    for i in range(1, ra, 2):
        print((i*".|.").center(m, '-'))
        _sum += i
        if _sum == ra:
            break
    print("WELCOME".center(m, '-'))
    _sum = 0
    for j in range(i, 0, -2):
        print((j*".|.").center(m, '-'))
