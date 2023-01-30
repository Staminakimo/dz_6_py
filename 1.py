# Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396
num = input("Введите число: ")

a = num+num
b = a+num
int_num = int(num)
int_a = int(a)
int_b = int(b)
print(f"{num} + {a} + {b} = {int_num + int_a +int_b}")
