class Person:
    def __init__(self, n):
        self.name = n

    def __add__(self, other):
        return self.name + ' love ' + other.name


m = Person('Маша')
p = Person('Коля')
x = m + p
print(x)
