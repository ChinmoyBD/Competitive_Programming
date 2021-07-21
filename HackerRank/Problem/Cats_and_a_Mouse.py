def catAndMouse(x, y, z):
    catA = z - x
    if catA < 0:
        catA -= catA * 2

    catB = z - y
    if catB < 0:
        catB -= catB * 2

    if catA == catB:
        return "Mouse C"
    elif catA < catB:
        return "Cat A"
    else:
        return "Cat B"


if __name__ == "__main__":
    for _ in range(int(input())):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        print(catAndMouse(x, y, z))
