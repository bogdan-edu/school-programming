def hello(name1, name2, years):
    if years >= 10:
        return name1 + ' дружить з ' + name2 + ' цілу вічність'
    else:
        return name1 + ' дружить з ' + name2 + ' ' + str(years) + ' років'


print(hello('Катя', 'Діана', 10))

