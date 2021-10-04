class Person:
    name = ''
    birth = 0

    def age(self, year):
        my_age = year - self.birth
        return my_age


bogdan = Person()
bogdan.name = 'Bogdan'
bogdan.birth = 1980

this_year = int(input('Який зараз рік? '))

print('Мене звати ', bogdan.name)
print('Мені ', bogdan.age(this_year), ' років')
