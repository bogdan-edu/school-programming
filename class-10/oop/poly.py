class Person:
    def __init__(self, n):
        self.name = n

    def __add__(self, other):
        return self.name + ' любить ' + other.name


male = Person('Вася')
female = Person('Ліза')
x = male + female
print(x)
