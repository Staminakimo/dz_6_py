# Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Н
# апишите программу, которая определяет, есть в массиве последовательность из трёх элементов,
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

random_list = list(random.randint(1, 10) for _ in range(10))
print(f'Наш список {random_list}')
n = input("Введите искомую комбинацию: ")
random_list = str(random_list).replace(",", '')
random_list = random_list.replace(" ", '')
if random_list.count(n):
    print("YES")
else:
    print("NO")
