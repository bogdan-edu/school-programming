my_word = input("Enter any word: ")
my_sym = list(my_word)
new_sym = []
new_word = ""

for i in range(len(my_sym)):
    new_element = my_sym[(len(my_sym) -1) - i]
    new_sym.append(new_element)
    new_word = new_word + str(new_sym[i])
print(new_word)
