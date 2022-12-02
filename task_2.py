# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


from random import randint
from typing import Optional

def random_list(list_size: int) -> list:
    '''
    Фунция поиска случайного числа
    '''
    list_rand = list()
    for i in range(list_size):
        list_rand.append(randint(-20, 20))
    return list_rand

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
            print('Вы ввели не число')   

def sum_search(lst):
    '''
    Функция получения суммы
    '''
    list_1 = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    list_2 = [lst[i]*lst[len(lst)-i-1] for i in range(list_1)]
    return(list_2)

proportions = give_int('Введите размерность: ', min_num = 1)
numbers = random_list(proportions)
new_list = sum_search(numbers)
print(f'Исходный список: {numbers}')
print(f'Новый список : {new_list}')

