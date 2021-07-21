t = int(input())
count = 0

for _ in range(t):
    st = input()
    if st == 'Tetrahedron':
        count += 4
    elif st == 'Cube':
        count += 6
    elif st == 'Octahedron':
        count += 8
    elif st == 'Dodecahedron':
        count += 12
    elif st == 'Icosahedron':
        count += 20

print(count)