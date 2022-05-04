# Написать программу которая получит имя и возраст пользователя, проверяя возраст >18 и
# выдает приветственное сообщение в зависимости от возраста
from random import randint

# name = input('Введите ваше имя: ')
# while True:
#     age = input('Введите ваш возраст: ')
#     if age.isdigit():
#         if int(age) >= 18:
#             print('Привет {}. Тебе доступен контент 18+.'.format(name))
#         break
#         else:
#             print('Привет {}. Контент 18+ тебе недоступен.'.format(name))
#         break
#     else:
#         print('Введите возраст коректно')

# Угадайка по твоим критериям
# lucky_numb = randint(1, 10)
# while True:
#     user_numb = input('Введите число от 1 до 10: ')
#     if user_numb.isdigit():
#         int_user_numb = int(user_numb)
#         if lucky_numb == int_user_numb:
#             print('Поздравляю, вы угадали число: {}.'.format(lucky_numb))
#             break
#         elif int_user_numb + 1 == lucky_numb or int_user_numb - 1 == lucky_numb:
#             print('Очень горячо')
#         elif int_user_numb + 2 == lucky_numb or int_user_numb - 2 == lucky_numb:
#             print('Горячо')
#         else:
#             print('Холодно')
#     else:
#         print('Введите число коректно')