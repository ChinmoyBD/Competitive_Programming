n = int(input())
st = []

for _ in range(n):
    st.append(input())
check = True
i_n = 0
for _ in range(n):
    for s in range(i_n, n-1):
        if st[s] not in st[s+1]:
            if st[s+1] in st[s]:
                st[s], st[s+1] = st[s+1], st[s]
                i_n = 0
            else:
                check = False
                break
    if not check:
        break
if not check:
    print("NO")
else:
    print("YES")
    for i in st:
        print(i)