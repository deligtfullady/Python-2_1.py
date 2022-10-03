'''Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)'''
n = int(input('Размер массива: '))
lst = []
for i in range(n):
    x = int(input('Введите число массива: '))
    lst.append(x)
print(lst)
import datetime
for i in range(0, len(lst)):
    j = datetime.datetime.now().microsecond % len(lst) - 1
    lst[i], lst[j] = lst[j], lst[i]
print(lst)