st = input().strip()

cap = ord(st[0])
if cap > 90:
    cap -= 32
    st = chr(cap) + st[1:]

print(st)