import random

qubes = int(input('Введіть кількість кубиків у грі '))


def bones(n):
    qube = [0]
    for i in range(n):
        qube.append(random.randint(1, 6))


    points = 0
    for i in range(1, n+1):
        points = points + qube[i]

    qube[0] = points

    return qube


gamer1 = bones(qubes)
gamer2 = bones(qubes)

if gamer1[0] > gamer2[0]:
    print('Переміг перший гравець')
elif gamer2[0] > gamer1[0]:
    print('Переміг другий гравець')
else:
    print('Нічия')

print('Перший гравець набрав ', gamer1[0], ' очок')
print('Другий гравець набрав ', gamer2[0], ' очок')
