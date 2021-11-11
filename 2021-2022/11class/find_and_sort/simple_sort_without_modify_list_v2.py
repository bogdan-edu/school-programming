my_list = [10, 100, 100, 8, 2, -100, 45, -1, -10, 5]

sorted_list = []

temp_list = list(my_list)

for i in range(len(temp_list)):
    min_el = temp_list[0]
    for el in temp_list:
        if el < min_el:
            min_el = el
    sorted_list.append(min_el)
    temp_list.remove(min_el)
print(sorted_list)
print(my_list)
