# d = int(input('Введите точность: '))
# calc_pi = 0
# check = 0
#
# for n in range(int(10000)):
#     calc_pi += (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
#     if abs(check - calc_pi) < 10**(-d):
#         break
#     check = calc_pi
#
# print('pi = ', round(calc_pi, d))

import math
import datetime
import os

# consts:

PRECISION_LIMIT = 1E-10
WARN_OUT_OF_RANGE = f'Число должно быть не больше 1 и не меньше {PRECISION_LIMIT}. Повторите.'


# methods:

def calc_pi_leibniz(precision):
    # precision = 10 ** (-(precision_digits + 1))
    precision /= 10
    d = 3
    sign = -1
    s = 4
    abs_addition = 1
    while abs_addition > precision:
        abs_addition = 4 / d
        s += sign * abs_addition
        sign = -sign
        d += 2
    return s


def calc_pi_bailey_borwein_plouffe(num_of_decimals):
    def formula(n):
        eight_n = n * 8
        sixteen_pow_n = 16 ** n
        return (4 / (eight_n + 1) - 2 / (eight_n + 4) - 1 / (eight_n + 5) - 1 / (eight_n + 6)) / sixteen_pow_n

    return sum([formula(i) for i in range(num_of_decimals + 1)])


def truncate(real_num, num_of_decimals):
    magnitude = 10 ** num_of_decimals
    real_num = math.trunc(real_num * magnitude)
    return real_num / magnitude


def num_of_decimals(real_num: float):
    if real_num == 0:
        return 100
    if real_num >= 1:
        return 0

    return int(math.ceil(math.log10(1 / real_num)))


def make_decimal_separator_invariant(expected_float_str: str) -> str:
    expected_float_str = expected_float_str.replace(',', '.')
    num_of_extra_dots = expected_float_str.count('.') - 1
    if num_of_extra_dots > 0:
        expected_float_str = expected_float_str.replace(
            '.', '', num_of_extra_dots)
    return expected_float_str


def get_user_input_float(prompt: str, warn_out_of_range: str, func_check_if_valid):
    not_a_number = False
    out_of_range = False
    while True:
        if not_a_number:
            not_a_number = False
            print("Некорректный ввод: Требуется вещественное число!")
        if out_of_range:
            out_of_range = False
            print(warn_out_of_range)

        try:
            inp = input(prompt)
            inp = make_decimal_separator_invariant(inp)
            num = float(inp)
            out_of_range = not func_check_if_valid(num)
            if not out_of_range:
                return num
        except:
            not_a_number = True


def ask_for_repeat():
    answer = input('Желаете повторить (Y/n)? ')
    return len(answer) == 0 or answer[0].lower() == 'y'


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# main flow:
user_answer = True

while (user_answer):
    console_clear()
    print(
        'Вычисление числа \u03c0 c заданной точностью'
        '\nТочность задаётся в виде вещественного числа вида 0.001')

    d = get_user_input_float('Введите вещественное число, обозначающее минимальную точность: ',
                             WARN_OUT_OF_RANGE, lambda a: a <= 1 and a >= PRECISION_LIMIT)

    decimal_places = num_of_decimals(d)
    print('\nРеференсное значение:\n')
    print('\u03c0 =', truncate(math.pi, decimal_places))

    print('\nРезультат вычисления с использованием ряда Лейбница:\n')

    start_time = datetime.datetime.now()
    pi = calc_pi_leibniz(d)
    elapsed_time = datetime.datetime.now() - start_time
    pi_truncated = truncate(pi, decimal_places)

    print('\u03c0 =', pi_truncated)
    print(f'\n(затрачено времени: {elapsed_time.total_seconds()} сек)')

    print('\nРезультат вычисления с использованием формула Бэйли—Боруэйна—Плаффа:\n')

    start_time = datetime.datetime.now()
    pi_2 = calc_pi_bailey_borwein_plouffe(decimal_places)
    elapsed_time = datetime.datetime.now() - start_time
    pi_2_truncated = truncate(pi_2, decimal_places)

    print('\u03c0 =', pi_2_truncated)
    print(f'\n(затрачено времени: {elapsed_time.total_seconds()} сек)')
    print()

    user_answer = ask_for_repeat()