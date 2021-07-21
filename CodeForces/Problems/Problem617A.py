def steps_count(f_h_located):
    count = 0
    while f_h_located > 0:
        if f_h_located >= 5:
            f_h_located -= 5
        elif f_h_located >= 4:
            f_h_located -= 4
        elif f_h_located >= 3:
            f_h_located -= 3
        elif f_h_located >= 2:
            f_h_located -= 2
        else:
            f_h_located -= 1

        count += 1
    print(count)


if __name__ == "__main__":
    x = int(input())
    steps_count(x)