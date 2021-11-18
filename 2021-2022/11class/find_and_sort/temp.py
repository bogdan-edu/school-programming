my_list = [10, 100, 100, 100, 8, 2, 45, -1, -10, 100,  5]

element = int(input("Шуканий елемент: "))
positions = []
for i in range(len(my_list)):
    if my_list[i] == element:
        positions.append(i + 1)


print(positions)