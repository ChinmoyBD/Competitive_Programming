salary = float(input())

if salary <= 400.00:
    par = 15
    earned = salary * par / 100
    print("New Salary: {:.2f}".format(earned + salary))
    print("Money earned: {:.2f}".format(earned))
    print(f"In percentage: {par} %")

elif salary <= 800.00:
    par = 12
    earned = salary * par / 100
    print("New Salary: {:.2f}".format(earned + salary))
    print("Money earned: {:.2f}".format(earned))
    print(f"In percentage: {par} %")

elif salary <= 1200.00:
    par = 10
    earned = salary * par / 100
    print("New Salary: {:.2f}".format(earned + salary))
    print("Money earned: {:.2f}".format(earned))
    print(f"In percentage: {par} %")

elif salary <= 2000.00:
    par = 7
    earned = salary * par / 100
    print("New Salary: {:.2f}".format(earned + salary))
    print("Money earned: {:.2f}".format(earned))
    print(f"In percentage: {par} %")

else:
    par = 4
    earned = salary * par / 100
    print("New Salary: {:.2f}".format(earned + salary))
    print("Money earned: {:.2f}".format(earned))
    print(f"In percentage: {par} %")


