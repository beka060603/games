class Fraction:

    def __init__(self, num, denum):
        if denum == 0:
            raise ValueError("Denominator can't 0!")
        self.num = num
        self.denum = denum

    def add(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        print(num)
        print("--")
        print(denum)

    def div(self, other):
        num = self.num * other.denum
        denum = self.denum * other.num
        print(num)
        print("--")
        print(denum)


    def mul(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        print(num)
        print("--")
        print(denum)

    def sub(self, other):
        num = self.num * other.denum - other.num * self.denum
        denum = self.denum * other.denum
        print(num)
        print("--")
        print(denum)

fraction1 = Fraction(7, 32)
fraction2 = Fraction(1, 12)
fraction1.sub(fraction2)
print()
fraction3 = Fraction(2,3)
fraction4 = Fraction(3,5)
fraction3.add(fraction4)