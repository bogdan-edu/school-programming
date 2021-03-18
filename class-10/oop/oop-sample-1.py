class Person:
    name = ''
    password = ''
    gender = ''

    def isadmin(self):
        if self.password == 'ahtung':
            return True
        else:
            return False

    def who(self):
        if self.gender == 'male':
            return 'він'
        elif self.gender == 'female':
            return 'вона'
        else:
            return 'воно'


admin = Person()
user = Person()
admin.name = 'Вася'
admin.password = 'ahtung'
user.name = 'Марфа'

print(user.isadmin())
print(admin.isadmin())

x = user.who()
y = admin.who()
print(x)
print(y)
