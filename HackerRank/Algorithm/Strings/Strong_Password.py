def minimumNumber(n, password):

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    num = l_c = u_c = s_c = 0

    for i in password:
        if i in numbers:
            num += 1
            continue
        elif i in lower_case:
            l_c += 1
            continue
        elif i in upper_case:
            u_c += 1
            continue
        elif i in special_characters:
            s_c += 1
    pp = 0
    if num == 0:
        pp += 1
    if l_c == 0:
        pp += 1
    if u_c == 0:
        pp += 1
    if s_c == 0:
        pp += 1

    return max(pp, 6-n)


if __name__ == "__main__":
    n = int(input())

    password = input()

    print(minimumNumber(n, password))