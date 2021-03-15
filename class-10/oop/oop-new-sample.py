class Animal:
    name = ''
    massa = 0
    speed = 0
    distance = 0
    def way(self, time):
        self. distance = self.speed * time
        return self. distance


tiger = Animal()
tiger.speed = 50
tiger.name = 'Тигр'
tiger.massa = 300

tiger.way(1)
print(tiger.name, ' пробіг ', tiger.distance, 'км')