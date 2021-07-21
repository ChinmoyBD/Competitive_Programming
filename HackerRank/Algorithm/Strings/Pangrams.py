def pangrams(s):
    s = s.lower()
    alp = [False] * 26
    for i in s:
        od = ord(i)
        if 97 <= od <= 122:
            if not alp[od-97]:
                alp[od-97] = True
    for b in alp:
        if not b:
            return "not pangram"
    return "pangram"


if __name__ == "__main__":
    s = input()
    print(pangrams(s))