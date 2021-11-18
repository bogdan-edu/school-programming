my_list = [10, 100, 100, 8, 2, 45, -1, -10, 5]

some_element = 8
count = -1
position = None
for el in my_list:
    count += 1
    # position = position + 1
    if el == some_element:
        position = count
        break

print(position)