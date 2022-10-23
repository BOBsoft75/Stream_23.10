import random

list_of_list = []

for i in range(5):
    new = []
    for k in range(5):
        new.append(str(random.randint(0,10)))
    list_of_list.append(new)

print(list_of_list)

for index, item in enumerate(list_of_list):
    list_of_list[index] = ';'.join(item)

print(list_of_list)

list_of_list = '\n'.join(list_of_list)
print(list_of_list)