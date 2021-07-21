st1 = input()
st2 = input()
st3 = input()

st1 += st2
st1 = sorted(st1)
st3 = sorted(st3)

if st1 == st3:
    print("YES")
else:
    print("NO")
