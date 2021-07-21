if __name__ == "__main__":
    t = int(input())
    if 2 <= t <= 6:
        li = []
        for _ in range(t):
            string = input().strip()
            n = float(input())
            li.append([string, n])
        li_s = sorted(li)
        li1 = []
        for i in range(len(li_s)):
            li1.append(li_s[i][1])
        _set = set(li1)
        set_list = list(_set)
        _min = min(set_list)
        for i in range(len(set_list)):
            if set_list[i] == _min:
                del set_list[i]
                break
        second_min = min(set_list)
        for i in range(len(li_s)):
            if li_s[i][1] == second_min:
                print(li_s[i][0])


