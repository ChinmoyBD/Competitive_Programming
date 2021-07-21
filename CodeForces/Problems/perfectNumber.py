def perfectNumber(start, stop):
    for i in range(start, stop+1):
        dSum = 1
        dList = [1]
        for d in range(2, int(i**0.5)+1):
            if i % d == 0:
                dSum += (d + i//d)
                dList.extend([d, i//d])
        if dSum == i:
            print(i)
            print(sorted(dList))


perfectNumber(20, 30)
perfectNumber(490, 500)