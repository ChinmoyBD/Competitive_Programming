class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores

    def calculate(self):
        res = sum(self.scores) // len(self.scores)

        if 90 <= res <= 100:
            return "O"
        elif 80 <= res < 90:
            return "E"
        elif 70 <= res < 80:
            return "A"
        elif 55 <= res < 70:
            return "P"
        elif 40 <= res < 55:
            return "D"
        elif res < 40:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName,lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())