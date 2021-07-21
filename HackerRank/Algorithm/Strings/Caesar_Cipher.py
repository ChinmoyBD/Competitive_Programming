def caesarCipher(s, k):
    ss = ''
    for i in s:
        or_d = ord(i)
        if 65 <= or_d <= 90:
            ss += chr(65 + (or_d+k-65) % 26)
        elif 97 <= or_d <= 122:
            ss += chr(97 + (or_d+k-97) % 26)
        else:
            ss += i
    return ss


if __name__ == "__main__":
    n = int(input())
    s = input()
    k = int(input())

    print(caesarCipher(s, k))