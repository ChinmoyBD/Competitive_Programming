def checking_m_or_f(name):
    if len(set(name)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    st = input()
    checking_m_or_f(st)