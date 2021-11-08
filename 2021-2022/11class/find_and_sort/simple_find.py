my_list = [10, 100, 100, 8, 2, 45, -1, -10, 5]

minimal_element = my_list[0]
position = 0
for i in range(len(my_list)):
    list_element = my_list[i]
    if list_element < minimal_element:
        minimal_element = list_element
        position = i
print(minimal_element)
print(position)