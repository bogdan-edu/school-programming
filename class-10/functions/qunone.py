import random
def qub():
    q1 = random.randint(1, 6)
    q2 = random.randint(1, 6)
    q = q1 + q2
    return q

if qub() % 2 == 0:
    print('Живи')
else:
    print('Ти наступив на міну')