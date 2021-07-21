def mod_divmod(a, b):
    return divmod(a, b)


def divison(a, b):
    return a // b


def modulo(a, b):
    return a % b


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    print(divison(n, m))
    print(modulo(n, m))
    print(mod_divmod(n, m))