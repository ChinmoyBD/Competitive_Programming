for _ in range(int(input())):
    n, a, b = map(int, input().split())

    sCount = aCount = 0
    event = "EQUINOX"
    for i in range(n):
        st = input().strip().upper()
        if st[0] in event:
            sCount += a
        else:
            aCount += b
    if sCount > aCount:
        print("SARTHAK")
    elif sCount < aCount:
        print("ANURADHA")
    else:
        print("DRAW")
