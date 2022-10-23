

# original_string = 'aaaaassssdddффжжжgggaaa'
#
# my_dict = {}
# result_string = ''
# for letter in original_string:
#     if not my_dict.get(letter):
#         my_dict[letter] = original_string.count(letter)
#         result_string += str(original_string.count(letter)) + str(letter)
# print(result_string)

# def rle_mtd(string: str) -> str:
#     """
#     Basic logic for encoding
#     :param string: str
#     :return: string_out: str
#     """
#     string_out = ''
#     count = 1
#     while string:
#         if len(string) > 1:
#             if string[0] == string[1]:
#                 count += 1
#                 string = string[1:]
#             else:
#                 string_out += str(count) + string[0]
#                 string = string[1:]
#                 count = 1
#         else:
#             string_out += str(count) + string[0]
#             string = ''
#
#     return string_out
#
#
# def rle_bck(string: str) -> str:
#     """
#     Basic logic for decoding
#     :param string: str
#     :return: string_out: str
#     """
#     string_out = ''
#     count = ''
#     while string:
#         if len(string):
#             if string[0].isdigit():
#                 count += string[0]
#                 string = string[1:]
#             else:
#                 count = int(count)
#                 string_out += string[0]*int(count)
#                 string = string[1:]
#                 count = ''
#         else:
#             break
#     return string_out
#
#
# print(rle_mtd('ABCABCABCDDDFFFFFF'))    # from wikipedia 1A1B1C1A1B1C1A1B1C3D6F
# print(rle_mtd('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))   # 9W3B24W1B14W
# print(rle_bck(rle_mtd('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')))
# print(rle_bck(rle_mtd('ABCABCABCDDDFFFFFF')))


string = '12f10a'

def encode(data_str: str):
    if data_str is None:
        return None
    if (data_len := len(data_str)) == 0:
        return ''
    encoded_str = ''
    series_char = data_str[0]
    count = 1
    i = 1
    while i < data_len:
        char = data_str[i]
        if char != series_char:
            encoded_str += str(count) + series_char
            series_char = char
            count = 1
        else:
            count += 1
        i += 1

    if count > 0:
        encoded_str += str(count) + series_char
    return encoded_str

def decode(data_str: str) -> tuple[str, list]:
    errors_found = []
    if data_str is None:
        return (None, errors_found)
    if (data_len := len(data_str)) == 0:
        return ('', errors_found)
    decoded_str = ''
    i = 0
    qty_str = ''
    while i < data_len:
        item = data_str[i]
        if item.isdigit():
            qty_str += item
        else:
            if qty_str == '':
                # сюда не должны попасть, если входящие данные корректные
                errors_found.append(i)
                # пропускаем индексы для которых следующий символ - буква,
                # пока не встретим цифру - начало нового блока (кол-во:символ)
                while i + 1 < data_len and not data_str[i + 1].isdigit():
                    i += 1
            else:
                # случай когда всё ОК:
                decoded_str += item * int(qty_str)
                qty_str = ''
        i += 1

    if qty_str != '':
        errors_found.append(data_len - 1)

    return (decoded_str, errors_found)

print(string)
print(decode(string))