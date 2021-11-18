my_list = [10, 100, 100, 8, 2, 45, -1, -10, 5]

some_element = 81
position = None
for i in range(len(my_list)):
    if my_list[i] == some_element:
        position = i
        break

print(position)