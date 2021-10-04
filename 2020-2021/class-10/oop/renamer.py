class Person:
    def __init__(self, n):
        self.name = n

    def rename(self, new_name):
        self.name = new_name


people = Person('Петро')
print(people.name)

people.rename('Павло')
print(people.name)

buba = Person('Буба')
print(buba.name)

buba.rename('Бубочка')
print(buba.name)