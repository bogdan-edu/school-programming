my_list = [10, 100, 100, 8, 2, -100, 45, -1, -10, 5]


def min_el(arg_list):
    min_el = arg_list[0]
    for el in arg_list:
        if el < min_el:
            min_el = el
    return min_el


sorted_list = []
for i in range(len(my_list)):
    el = min_el(my_list)
    sorted_list.append(el)
    my_list.remove(el)
print(sorted_list)
