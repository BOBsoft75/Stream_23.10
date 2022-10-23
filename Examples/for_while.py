
# string = 'asdfdshgdfjj'
#
# letter = input('Введите букву: ')
#
# for i, symb in enumerate(string):
#     if letter == symb:
#         print(f'Символ {symb} стоит на позиции {i}')
#         break
# else:
#     print('Искомой буквы нет в данном тексте')

my_list = [(x+5)**2 for x in range(10)]

print(my_list)

for item in my_list:
    item += 1

print(my_list)

for i in range(len(my_list)):
    my_list[i] += 1

print(my_list)

for i,item in enumerate(my_list, start=0):
    if item < 101:
        my_list[i] = 52

print(my_list)

new_list = list(map(lambda x:x*1000, my_list))

one_more_list = list(map(lambda x: x%2 != 0, my_list))
two_more_list = list(filter(lambda x: x%2 != 0, my_list))
three_more_list = list(filter(lambda x: x%2 != 0, my_list))



one_list = [(x+5)**2 for x in range(10)]
two_list = [(x+5)**2 for x in range(10,13)]
three_list = [(x+5)**2 for x in range(100,110)]
four_list = [(x+5)**2 for x in range(-10,0)]

big_list = list(zip(one_list, two_list, three_list, four_list))

print(big_list)



print(one_more_list)
print(two_more_list)

print(new_list)