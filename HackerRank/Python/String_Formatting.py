def print_formatted(number):
    for i in range(1, number + 1):
        decimal = i
        octal = oct(i)
        hexadecimal = hex(i).upper()
        binary = bin(i)

        print("{}  {}  {}  {}".format(decimal, octal[2:], hexadecimal[2:], binary[2:]))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


