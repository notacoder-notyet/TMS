# Сделать свой декоратор
# Сделать лямбда функцию
# Сделать функцию и обернуть декоратором

def decorator(func):
    def wrapper():
        print('Я верхняя обертка декоратора')
        func()
        print('Я нижняя обертка декоратора')
    return wrapper

@decorator
def test():
    print('Я функция')

test()


# c = lambda n: lambda k: n*k
# a = c(4)
# """Число которое умножаем"""
# a(5)
# """Число на которое умножаем"""
# print(a(5))

