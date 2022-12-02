# Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number_list = [2, 3, 5, 9, 3, 8, 10]
print(number_list)
list_length = len(number_list)
sum_result_even = 0
sum_result_not_even = 0

for i in range(list_length):
    if i%2 == 0:
        sum_result_even += number_list[i]
    if i%2 == 1:
        sum_result_not_even += number_list[i]

print(f'Сумма четных элементов: {sum_result_even}')
print(f'Сумма нечетных элементов: {sum_result_not_even}')