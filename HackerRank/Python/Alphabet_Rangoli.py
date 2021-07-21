import string
def print_rangoli(n):
    alpha = string.ascii_lowercase
    s_l = (n - 1) * 2
    s_r = (s_l + s_l) + 1
    li = []
    for i in range(n):
        s = '-'.join(alpha[i:n])
        li.append(s[::-1]+s[1:])
    for i in range(n-1, 0, -1):
        print(li[i].center(s_r, '-'))

    for i in range(n):
        print(li[i].center(s_r, '-'))

if __name__ == '__main__':

    n = int(input())
    print_rangoli(n)

