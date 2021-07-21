def lcd(a, b):
    if a % b == 0:
        return b
    return lcd(b, a%b)


li = [12, 42, 54]
a = l = li[0]
for i in range(1, 3):
    b = li[i]
    a = lcd(a, b)
    l = (l*b)//a

print("GCD = {}, LCM = {}".format(a, l))