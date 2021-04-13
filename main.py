class Complex:

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        real = self.real + other.real
        image = self.image + other.image
        new_com = Complex(real, image)
        return new_com

    def __mul__(self, other):
        real = self.real * other.real
        image = self.image * other.image
        new_com = Complex(real, image)
        return new_com

    def __sub__(self, other):
        real = self.real - other.real
        image = self.image - other.image
        new_com = Complex(real, image)
        return new_com

    def __truediv__(self, other):
        real = self.real / other.real
        image = self.image / other.image
        new_com = Complex(real, image)
        return new_com

c1 = Complex(1,2)
c2 = Complex(1,6)
c3 = c1 * c2
c4 = c1 + c2
c5 = c1 - c2
c6 = c1 / c2
print(c3.real)
print(c3.image)
print()
print(c4.real)
print(c4.image)
print()
print(c5.real)
print(c5.real)
print(c6.image)
print(c6.image)


