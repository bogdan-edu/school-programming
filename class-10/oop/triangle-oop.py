class Triangle:
    a = 0
    b = 0
    c = 0

    def perimeter(self):
        return self.a + self.b + self.c

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


triangle = Triangle()

triangle.a = 3
triangle.b = 4
triangle.c = 5

# triangle.a = float(input('a = '))
# triangle.b = float(input('b = '))
# triangle.c = float(input('c = '))

print('Периметр: ', triangle.perimeter())
print('Рівнобедренний: ', triangle.isosceles())
print('Прямокутний: ', triangle.rectangular())
