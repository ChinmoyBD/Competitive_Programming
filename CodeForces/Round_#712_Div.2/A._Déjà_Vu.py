for _ in range(int(input())):
    st = input().strip()

    le_n = len(st)

    if st.count('a') == le_n:
        print("NO")
    elif 'a'+st == ('a'+st)[::-1]:
        print("YES")
        print(st+'a')
    else:
        print("YES")
        print('a'+st)
