# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

from typing import Optional

def give_int(input_number:  str,
            min_num: Optional[int] = None,
            max_num: Optional[int] = None) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number)) 
            if min_num and num < min_num:
                print(f'Введите число больше или равно: {min_num}')
                continue  
            if max_num and num > max_num:
                print(f'Введите число меньше или равно: {max_num}')
                continue 
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

def negafibonacci(num: int) -> list:
    '''
    Функция построения списка Фибоначчи(Негафибоначчи)
    '''
    fib_list = [0]
    positive = 0
    negative = 1
    minus = 1

    for i in range(1, num + 1):  
        positive, negative = negative, positive + negative  
        fib_list.append(positive)   
        fib_list.insert(0, minus * positive)
        minus *= -1
    return fib_list

int_number = give_int('Введите число: ', min_num = 1, max_num = 15)
result = negafibonacci(int_number)
print(result)
