some_string = 'microsoft Word'
str_list = some_string.split(' ')
str_list[0] = str_list[0].capitalize()
some_string = ' '.join(str_list)
print(some_string)