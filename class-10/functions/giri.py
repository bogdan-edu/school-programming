a1 = int(input('Учень 1  10-А класу підняв гирю разів: '))
a2 = int(input('Учень 2  10-А класу підняв гирю разів: '))
a3 = int(input('Учень 3  10-А класу підняв гирю разів: '))
a4 = int(input('Учень 4  10-А класу підняв гирю разів: '))
a5 = int(input('Учень 5  10-А класу підняв гирю разів: '))

b1 = int(input('Учень 1  10-Б класу підняв гирю разів: '))
b2 = int(input('Учень 2  10-Б класу підняв гирю разів: '))
b3 = int(input('Учень 3  10-Б класу підняв гирю разів: '))
b4 = int(input('Учень 4  10-Б класу підняв гирю разів: '))

x = (a1 + a2 + a3 + a4 + a5) - (b1 + b2 + b3 +b4)

print('Різниця кількості піднімань гирі між класом А та класом Б', x, 'разів')