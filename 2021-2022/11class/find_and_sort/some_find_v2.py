my_list = [10, 100, 100, 8, 2, 45, -1, -10, 5]

some_element = 8
position = None
for el in my_list:
    if el == some_element:
        position = my_list.index(el)
        break

print(position)