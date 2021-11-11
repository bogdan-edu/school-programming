my_list = [10, 100, 100, 8, 2, -100, 45, -1, -10, 5]

sorted_list = []
for i in range(len(my_list)):
    max_el = my_list[0]
    for el in my_list:
        if el > max_el:
            max_el = el
    sorted_list.append(max_el)
    my_list.remove(max_el)
print(sorted_list)
print(my_list)
