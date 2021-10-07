deposit = int(input('Сума вкладу: '))
percent = int(input('Під який відсоток депозит: '))
main_sum = int(input('Сума сума після повернення: '))

years = 0

while deposit < main_sum:
    years += 1
    deposit = deposit + percent * deposit / 100
    print(f'Через {years} років депозит буде {deposit}')

print(f'Необхідної суми ми досягнемо через {years} років')
