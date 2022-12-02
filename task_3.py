# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from random import random, randint
from typing import Optional

def random_list_float(list_size: float) -> list:
    '''
    Фунция поиска случайного вещественного числа
    '''
    list_random = list()
    for i in range(list_size):
        list_random.append (round(random() + randint(1, 20), 2))
    return list_random

def give_int(input_string: str,
            min_num: Optional[int] = None) -> int:
    '''
    Функция заполнения списка
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите число больше {min_num}')
                continue   
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

def diff_search(lst):
    '''
    Функция поиска разницы
    '''
    list_1 = [round(i%1,2) for i in lst if i%1 != 0]
    diff_results =  round(max(list_1) - min(list_1), 2)
    return(diff_results)

proportions = give_int('Введите размерность: ', min_num = 1)
numbers = random_list_float(proportions)
result = diff_search(numbers)
print(f'Исходный список: {numbers}') 
print(f'Разница: {result}')         