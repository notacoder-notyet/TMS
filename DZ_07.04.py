try:
    try:
        x = float(input('Введите первое число: '))
    except ValueError:
        print('Вы ввели не число')
    try:
        y = float(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели не число!')
    s = input('Введите знак (+, -, *, /): ')
    if s in ('+', '-', '*', '/'):
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
            try:
                y != 0
                print(x/y)
            except ZeroDivisionError:
                print('Деление на ноль невозможно!')
    else:
        print('Неверный знак операции!')
except NameError:
    print('Одно из значений оказалось не числом')

