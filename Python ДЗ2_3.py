'''Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
Пример: Для n = 5: сумма = 11,55'''
n = int(input('Введите число: '))
lst = []
x = 1
for i in range(n):
    lst.append((1+(1/x))**x)
    x += 1
sum = 0
for i in lst:
    sum = sum + i
print('сумма =', round(sum, 2))