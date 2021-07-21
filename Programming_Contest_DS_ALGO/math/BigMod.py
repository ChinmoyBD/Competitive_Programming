
def bigMod(a, b, m):
    if b == 0:
        return 1 % m
    x = bigMod(a, b//2, m)
    x = (x*x) % m
    if b % 2 == 1:
        x = (x * a) % m
    return x


def test1():
    print(bigMod(10767, 20078934, 5))


def test2():
    print((10767 ** 20078934) % 5)


test1()
test2()