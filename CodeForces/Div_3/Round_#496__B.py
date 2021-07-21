a = input()
b = input()

le_a = len(a)
le_b = len(b)
# ai = bi = 0
n = le_a + le_b
count = 0

while True:
    ai = le_a - count - 1
    bi = le_b - count - 1
    if ai >= 0 and bi >= 0 and a[ai] == b[bi]:
        count += 1
    else:
        break

print(n - count*2)