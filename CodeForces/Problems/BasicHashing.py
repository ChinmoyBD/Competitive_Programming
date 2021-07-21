def convert(egId):
    idNumber = ''
    count = 0
    tpS = ''
    idSum = 0

    for i in egId:
        if count > 2:
            tpS += i
            if len(tpS) == 2:
                if count == 4:
                    idNumber += tpS
                else:
                    idNumber += f"+{tpS}"
                idSum += int(tpS)
                tpS = ''
        count += 1

    idSum += int(tpS)
    idSum %= 100
    if idSum < 10:
        idSum = '0' + str(idSum)

    idNumber += f"+{tpS} = {idSum}"

    print(idNumber)


convert('CSE202003029')