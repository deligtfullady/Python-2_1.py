'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.'''
n = int(input('Введите число: '))
lst = []
for i in range(-n, n+1):
    lst.append(i)
print(lst)
f = open('file.txt')
ind1 = int(f.read(1))
ind2 = int(f.read(2))
f.close()
print(ind1, 'and', ind2)
mult = lst[ind1] * lst[ind2]
print(lst[ind1], '*', lst[ind2], '=', mult)