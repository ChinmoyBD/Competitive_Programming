def binary(n):
    b = bin(n)
    b = b[2:]
    one, one_one = 0, 0

    for i in b:
        if i == '1':
            one += 1
        else:
            if one_one < one:
                one_one = one
            one = 0
    if one_one < one:
        one_one = one

    return one_one


if __name__ == "__main__":
    n = int(input())
    print(binary(n))