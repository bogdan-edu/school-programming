import random

gamer1_qube1 = random.randint(1, 6)
gamer1_qube2 = random.randint(1, 6)
gamer1_points = gamer1_qube1 + gamer1_qube2

gamer2_qube1 = random.randint(1, 6)
gamer2_qube2 = random.randint(1, 6)
gamer2_points = gamer2_qube1 + gamer2_qube2

if gamer1_points > gamer2_points:
    print('Переміг перший гравець')
elif gamer2_points > gamer1_points:
    print('Переміг другий гравець')
else:
    print('Нічия')
