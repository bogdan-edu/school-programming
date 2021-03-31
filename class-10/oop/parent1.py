class Person:
    def __init__(self, n):
        self.name = n

    def rename(self, new_name):
        self.name = new_name


class Friend(Person):
    def __init__(self, n, a):
        super().__init__(n)
        self.address = a

    def relocation(self, a):
        self.address = a



