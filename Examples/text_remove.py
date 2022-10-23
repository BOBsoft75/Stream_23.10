string = 'Ладно, сердечно благодарю за стрим, пойду. Надо отдохнуть, а то на работу через полтора часа + буткемп. Голова плавится)))'

print(string)
letter = input('Введите букву: ')

sub_string = string.replace(',', ' , ').replace('.', ' . ')
new_string = string.lower().replace(f'{letter}', '')

print(new_string)

words = sub_string.split()
print(words)

new_words = []

for word in words:
    if letter not in word.lower():
        new_words.append(word)

new_words = ' '.join(new_words)
print(new_words)


StRiNg = 'АбаВЫОАжьмЫУВЬасЖЫАУЦ'
print(StRiNg.lower())
print(StRiNg.upper())