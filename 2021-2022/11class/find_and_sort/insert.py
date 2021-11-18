my_list = [10, 100, 100, 100, 8, 2, 45, -1, -10, 100,  5]

sorted_list = sorted(my_list)
print(sorted_list)

el = int(input('el = '))

for i in range(len(sorted_list)):
    if (el > sorted_list[i]) and (el < sorted_list[i+1]):
        sorted_list.insert(i+1, el)

print(sorted_list)
