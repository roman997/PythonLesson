import math

#Завдання 1


def task1(x):
    z = 0
    for number in x:
        z = z + int(number)
    s = float(z / len(x))
    return s


e = input('Введіть числа : ')
b = task1(e)
print(f'Середнє арифметичне значення масиву: {b}')

# Завдання 2
#
#
# def task2(*args):
#     z = 0
#     for number in args:
#         z += int(number)
#     return z
#
#
# b = task2(8, 2, 3, 5)
# print(f'Середнє арифметичне значення масиву: {b}')
#
#
# # Завдання 3
#
#
# def task3(x):
#     m = math.factorial(x)
#     return m
#
# b = input('Введіть число: ')
# print(task3(int(b)))
#
#
# # Завдання 4

#
# def task4(x):
#     m = math.factorial(x)
#     return m
#
# b = input('Введіть число: ')
# print(task3(int(b)))


z = lambda b: b**b
print(z(int(input('Введіть число :'))))