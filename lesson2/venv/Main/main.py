#Завдання 1
#
#
# def first(s):
#
#     d = s[-1]
#     a = ''
#     for char in s:
#         if char != d:
#             a = a + char
#     return a
#
#
# x = str(input("Введіть стрічку : "''))
# print(first(x))

# #Завдання 2
# x = int(input('Введіть число: '))
# i = 0
# while i <= x:
#     print(i)
#     i = i + 1
#
#
# #Завдання 3
#
#
# def nsd(a, b):
#     if b != 0:
#         return nsd(b, a % b)
#     else:
#         return a
#
#
# x = int(input('Введіть перше число : '))
# y = int(input('Введіть друге число : '))
# print("Спільне кратне : ", x * y // nsd(x, y))
#
#
# #Завдання 4
# x = input('Введіть число : ')
# y = [x]
# x = str(input('Введіть наступні числа : '))
# for char in x:
#     y.append(char)
# z = 0
# for number in y:
#     z = z + int(number)
# s = float(z / len(y))
# print(s)
