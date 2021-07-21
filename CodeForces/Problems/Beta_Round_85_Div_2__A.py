def petya_loves(s1, s2):
    if s1 == s2:
        print(0)
    elif s1 < s2:
        print(-1)
    elif s1 > s2:
        print(1)


if __name__ == "__main__":
    s1 = input().lower()
    s2 = input().lower()

    petya_loves(s1, s2)