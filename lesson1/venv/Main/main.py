print("Hello World")


x = int (input('Введіть перше число: '))
operation = input('Введіть знак (+,-,*,/): ')
y = int(input('Введіть друге число: '))

if operation == '+':
	print(f'{x} {operation} {y} = {x + y}')
elif operation == '-':
    print(f'{x} {operation} {y} = {x-y}')
elif operation == '*':
	print(f'{x} {operation} {y} = {x*y}')
elif operation == '/':
	print(f'{x} {operation} {y} = {x / y}')
