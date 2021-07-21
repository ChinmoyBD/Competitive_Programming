def gradingStudents(grades):
    li = []
    for i in grades:
        if i + 5 < 40:
            li.append(i)
        else:
            for j in range(i, i + 6):
                if j % 5 == 0:
                    m = j - i
                    if m < 3:
                        li.append(i + m)
                        break
                    else:
                        li.append(i)
                        break

    print(li)


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
