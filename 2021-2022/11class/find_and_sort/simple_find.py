my_list = [10, 100, 100, 8, 2, 45, -1, -10, 5]

minimal_element = my_list[0]
position = 0
for i in range(len(my_list)):
    if my_list[i] < minimal_element:
        minimal_element = my_list[i]
        position = i
print(minimal_element)
print(position)