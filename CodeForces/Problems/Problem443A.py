st = input()
se_t = set()
for s in st:
    if s != ',' and s != '{' and s != '}' and s != ' ':
        se_t.add(s)


print(len(se_t))