class Rectangular:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def rect_square(self):
        return self.a * self.b


class Triangle(Rectangular):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.a = x
        self.b = y

    def square(self):
        return self.rect_square() / 2


figure = Triangle(3, 4)
s = figure.square()

print('s = ', s)
