bn1 = input()
bn2 = input()

result = ''
for i in range(len(bn1)):
    if bn1[i] == bn2[i] == '1' or bn1[i] == bn2[i] == '0':
        result += '0'
    else:
        result += '1'
print(result)