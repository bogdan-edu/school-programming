import random

kydaty = 'y'
while kydaty == 'y':
    q1 = random.randint(1, 6)
    q2 = random.randint(1, 6)
    q = q1 + q2
    print('Випало', q)
    kydaty = input('Кинути кубики ще раз? ( якщо так, введіть "Y", інакше натисніть "Enter") ')