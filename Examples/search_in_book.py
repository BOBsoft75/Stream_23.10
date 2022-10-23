phone_book = ['Барсук, 555, xthn',
                'Лиса, 949, рыжая',
                'Слон, 999, большой',
                'Орел, 333, домашний',
                'Волк, 878, серый']

print(phone_book)

search = input('Что ищем? ')
found = False
new_list = []
for item in phone_book:
    if search.lower() in item.lower():
        new_list.append(item)
        found = True
if not found: print('Ничего не найдено!')

print(new_list[0].upper())
