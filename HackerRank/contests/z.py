n = int(input())
width = n
print('*'*n)

while width > 2:
    width -= 1
    print('*'.rjust(width,' '))

print('*'*n)