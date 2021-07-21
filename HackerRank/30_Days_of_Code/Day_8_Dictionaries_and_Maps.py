t = int(input())
dc = {}

for _ in range(t):
    nm = input().strip().split()

    dc[nm[0]] = nm[1]

while True:
    try:
        st = input().strip()

        if st in dc:
            print("{}={}".format(st, dc[st]))
        else:
            print("Not found")
    except: break
