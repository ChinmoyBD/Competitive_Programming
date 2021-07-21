class AdvancedArithmetic(object):
    def divisorSum(self, n):
        return NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s_um = 0
        for i in range(1, n+1):
            if n % i == 0:
                s_um += i

        return s_um


if __name__ == "__main__":
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisorSum(n)
    print("I implemented: " + type(my_calculator).__base__[0].__name__)
    print(s)