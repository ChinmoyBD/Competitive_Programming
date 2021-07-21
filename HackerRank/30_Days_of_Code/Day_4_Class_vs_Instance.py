class Person:
    def __init__(self, initialAge):
        self.Age = initialAge
        if self.Age < 0:
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        if self.Age < 13:
            print("You are young.")
        elif self.Age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.Age += 1


t = int(input())
for i in range(t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(3):
        p.yearPasses()
    p.amIOld()
    print("")