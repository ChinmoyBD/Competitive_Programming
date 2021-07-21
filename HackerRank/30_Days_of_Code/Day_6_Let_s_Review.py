if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        s = input()
        even_s = ''
        odd_s = ''
        for i in range(len(s)):
            if i % 2 == 0:
                even_s += s[i]
            else:
                odd_s += s[i]

        print(even_s, odd_s)
