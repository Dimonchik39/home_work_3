# Напишите программу, которая будет преобразовывать десятичное число
#  в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

from typing import Optional

def give_int(input_number:  str,
            min_num: Optional[int] = None) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number)) 
            if min_num and num < min_num:
                print(f'Введите число больше {min_num}')
                continue   
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

def trans_num(int_num):
    '''
    Функция преобразования десятичного числа в двоичное
    '''
    dec_num = int_num
    bin_num = ''
    while dec_num != 0:
        bin_num = str (dec_num % 2) + bin_num
        dec_num //=2
    return bin_num

int_number = give_int('Введите десятичное число: ', min_num = 1)
result = trans_num(int_number) 
print(f'Число  в  двоичной системе: {result}') 