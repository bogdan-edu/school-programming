def sex(g):
    if g == 'm':
        return ', який ти гарний'
    elif g == 'f':
        return ', яка ти гарна'
    else:
        return ', ти що таке?'

name = input('Привіт, як тебе звати? ')
gender = input('ти хлопчик(m) чи дівчинка(f) ')
print(name, sex(gender))