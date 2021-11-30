my_list = [3, 9, 12, 22, 23, 27, 28, 39, 45, 50, 58, 60, 61, 73, 76, 85, 89, 92, 94, 99]

some_element = 85
position = None
for i in range(len(my_list)):
    if my_list[i] == some_element:
        position = i
        break

print(position)