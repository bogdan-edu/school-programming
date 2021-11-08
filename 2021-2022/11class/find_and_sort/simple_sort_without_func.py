my_list = [10, 100, 100, 8, 2, -100, 45, -1, -10, 5]


sorted_list = []
for i in range(len(my_list)):
    min_el = my_list[0]
    for el in my_list:
        if el < min_el:
            min_el = el
    sorted_list.append(min_el)
    my_list.remove(min_el)
print(sorted_list)
print(my_list)