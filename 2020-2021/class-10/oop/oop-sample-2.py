class Samp:
    def __init__(self, p='предмет', k=0):
        self.predm = p
        self.klas = k

    def func1(self, a1):
        self.predm = a1

    def func2(self, a2):
        self.klas = a2


ob1 = Samp('інформатика', 10)
ob2 = Samp()

print(ob1.predm, ob1.klas)
print(ob2.predm, ob2.klas)

ob1.func1('математика')
ob2.func1('історія')
ob2.func2(9)

print(ob1.predm, ob1.klas)
print(ob2.predm, ob2.klas)
