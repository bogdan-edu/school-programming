class Person:
    def __init__(self, n):
        self.name = n

    def rename(self, new_name):
        self.name = new_name


class Friend(Person):
    address = ''

    def relocation(self, a):
        self.address = a


people = Person('Петро')
print(people.name)

people.rename('Павло')
print(people.name)

buba = Friend('Буба')
print(buba.name)

buba.rename('Бубочка')
print(buba.name)

print(buba.address)

buba.relocation('Жмеринка')
print(buba.address)
