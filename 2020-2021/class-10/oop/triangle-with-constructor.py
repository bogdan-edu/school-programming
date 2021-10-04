class Triangle:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    def isosceles(self):
        if self.a == self.b:
            return True
        elif self.a == self.c:
            return True
        elif self.b == self.c:
            return True
        return False

    def rectangular(self):
        if self.a ** 2 + self.b ** 2 == self.c ** 2:
            return True
        elif self.a ** 2 + self.c ** 2 == self.b ** 2:
            return True
        elif self.b ** 2 + self.c ** 2 == self.a ** 2:
            return True
        return False


# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))

# triangle = Triangle(a, b, c)
triangle = Triangle(3, 4, 5)

print('Периметр: ', triangle.perimeter())
print('Рівнобедренний: ', triangle.isosceles())
print('Прямокутний: ', triangle.rectangular())
