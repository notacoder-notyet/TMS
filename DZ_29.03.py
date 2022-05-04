# f = open ('users.txt', 'w')
# f.write('Hi, it\'s me!/s')
# f.close()
# f = open ('users.txt')
# print(f.read(1))
# for line in f:
#     print(line)
# f.close()

# import json

# users_name = []
name = input('Введите имя: ')
# users_name.append(name)
# ages = []
age = input('Введите ваш возраст: ')
# ages.append(age)
# to_write = {'Name': users_name, 'Ages': ages}

# with open('users.json', 'w') as f:
#     f.write(json.dumps(to_write))

# with open('users.json') as f:
#     print(f.read())
# f.close()

# import csv
# with open("users.csv", mode="w", encoding='utf-8') as f:
#     names = ['Name', 'Age']
#     file_writer = csv.DictWriter(f, delimiter = ",", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({'Name': name, 'Age': age})
# with open('users.csv', encoding='utf-8') as f:
#     file_reader = csv.DictReader(f, delimiter = ',')
#     count = 0
#     for row in f:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#             print(f' {row['Name']} - {row['Age']}', end='') #Ругаеться, не понимаю почему. Форматирование вроде должно из списка идти, но просит строку. Хотя row строка
#         count += 1
# f.close