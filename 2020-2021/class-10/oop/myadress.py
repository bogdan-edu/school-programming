class Person:
    name = ''
    address = ''

    def hello(self):
        print('Привіт, мене звати ', self.name)

    def tohome(self):
        return 'Мене звати ' + self.name + ', я живу в ' + self.address

man = Person()
man.name = 'Вася'
man.address = 'село Білоцерківка'

man.hello()

togo = man.tohome()
print(togo)