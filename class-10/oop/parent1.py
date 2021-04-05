class Person:
    def __init__(self, n):
        self.name = n

    def rename(self, new_name):
        self.name = new_name


class Freind(Person):
    def __init__(self, n, a):
        super().__init__(n)
        self.address = a

    def relocation(self, a):
        self.address = a


buba = Person('Буба')
print(buba.name)
buba.rename('Бубася')
print(buba.name)

buba_freind = Freind('Буба', 'Білоцерківка')
print(buba_freind.name)
print(buba_freind.address)

buba_freind.relocation('Жмеринка')
buba_freind.rename('Бубочка')
print(buba_freind.name)
print(buba_freind.address)
