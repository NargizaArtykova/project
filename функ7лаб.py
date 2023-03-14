#7.1
students = {}
students.setdefault('Anna', {'age': 20, 'major': 'Biologist'})
students.setdefault('Tom', {'age': 18, 'major': 'Math'})
students.update({'Anna': {'age': 21, 'major': 'Math'}})
anna_major = students.get('Anna', {}).get('major')
print(f'Anna: спец - {anna_major}')

removed_student = students.pop('Tom')
print(f'pop: {removed_student}')

clear_student_dict = students.clear()
print(clear_student_dict)

#7.2.1
'''
2
Корея: Кымган, Тэхва, Хенсанган
Канада: Маккензи, Йукон, Сен-Лоурен
Волга, Парана, Лена
Маккензи
Италия: нрпглр

'''


n = int(input())
countries = {}
for i in range(n):
    # Считываем строку вида "Страна: река1, река2, ..."
    country_data = input().split(": ")
    # Разделяем названия рек и сохраняем их в списке
    rivers = country_data[1].split(", ")
    # Записываем название страны и список рек в словарь
    countries[country_data[0]] = rivers

river_names = input().split(", ")

#вывод стран, в которых протекает каждая река
for river_name in river_names:
    for country_name, rivers in countries.items():
        if river_name in rivers:
            print(f"{river_name} протекает в {country_name}")

#проверка наличия реки в словаре
check_river_name = input()
if any(check_river_name in rivers for rivers in countries.values()):
    print(f"Река {check_river_name} присутствует в словаре")
else:
    print(f"Река {check_river_name} отсутствует в словаре")

#добавление новой пары страна-река в словарь
new_country_name, new_river_name = input().split(": ")
if new_country_name in countries:
    countries[new_country_name].append(new_river_name)
else:
    countries[new_country_name] = [new_river_name]

print(countries)

#7.2.2
commentators = {}
while True:
    line = input()
    if not line:
        break
    name, comment = line.split(": ")
    commentators[name] = None

print(len(commentators))

#7.2.3

n = int(input())
phone_book = {}
for i in range(n):
    phone, name = input().split()
    phone_book[name] = phone
query = input()
if query in phone_book:
    print(phone_book[query])
else:
    print("Нет в телефонной книге")

#7.2.4
'''
2
Артыкова 3 июля
Аманжолов 14 мая
май

'''

n = int(input()) # количество сотрудников
vacations = {} # словарь для хранения графика отпусков

# заполнение словаря
for i in range(n):
    name, day, month = input().split()
    if month not in vacations:
        vacations[month] = [name]
    else:
        vacations[month].append(name)

# обработка запроса
query_month = input()
if query_month in vacations:
    print(" ".join(vacations[query_month]))
else:
    print()
