def step1(a, b):
    if a == 0 or b == 0:
        return a, b
    else:
        return step2(a, b)


def step2(a, b):
    if a >= 2*b:
        a = a - (2*a)
        return step1(a, b)
    else:
        return step3(a, b)


def step3(a, b):
    if b >= 2*a:
        b = b - (2*a)
        return step1(a, b)

    else:
        return a, b


if __name__ == "__main__":
    a, b = map(int, input().split())

    print(step1(a, b))