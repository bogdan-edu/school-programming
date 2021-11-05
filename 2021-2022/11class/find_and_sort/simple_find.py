my_list = [10, 100, -100, 8, 2, 45, -1, -10, 5]

minimal_element = my_list[0]
for list_element in my_list:
    if list_element < minimal_element:
        minimal_element = list_element
print(minimal_element)