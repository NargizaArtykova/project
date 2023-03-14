#5.1
person = ['Артыкова Наргиза']
citizenship = ['Гражданство - Казахстан']
email = ['artykova_n01@mail.ru']
p_num = ['+7 747 202 39 31']
job = ['Trainee programmer', '40 000 T']
experience = []
education = ['Satbayev University', '2020-2024']
language = ['Казахский - Родной', 'Русский - В совершенстве']
e = [1, 2, 'Опыт работы 3 месяца', 'Too Fashion Retail Kazakhstan']
l = ['Учусь в 3-курсе на факультете програмной инженерий', 'C++', 'C#', 'Dart', 'JS', 'Python', 'HTML', 'CSS', 'Postgresql']
person.append(21)
experience.extend(e)
experience.extend(l)
experience.insert(1, 'Продавец консультант')
experience.remove(2)
experience.pop(0)
print(person)
print(citizenship)
print(p_num)
print(job)
print(experience)
print(education)
print(language)

#5.2.1
class Student(object):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def __repr__(self):
        return  self.subject


student1 = Student('Anna', 'Algorithm')
student2 = Student('Alice', 'Math')
student3 = Student('Tom', 'Algebra')
students = [student1, student2, student3]

def bysubject(student):
    return student.subject

result = sorted(students, key=bysubject)
print(result)

#5.2.2
subjects = [0, 'english','history','math']
Anna_grades = ['Anna',85, 84, 86]
Tom_grades = ['Tom',96, 98, 92]
Bob_grades = ['Bob',95, 84, 75]
n = input()
for i in range(1, len(subjects)):
    if(Anna_grades[0] == n):
        print(subjects[i], '-' ,Anna_grades[i])
    if(Tom_grades[0] == n):
        print(subjects[i], '-' ,Tom_grades[i])
    if(Bob_grades[0] == n):
        print(subjects[i], '-' ,Bob_grades[i])

#5.2.3
data = []
num = int(input("Введите целое число (0 для окончания ввода): "))
while num != 0:
    data.append(num)
    num = int(input("Введите целое число (0 для окончания ввода): "))
print(*sorted(data), sep=' ')

#5.2.4
data = []
num = int(input("Введите целое число (0 для окончания ввода): "))
while num != 0:
    data.append(num)
    num = int(input("Введите целое число (0 для окончания ввода): "))
print(*sorted(data, reverse=True), sep=' ')

#5.2.5
from random import randrange
MIN_NUM = 1
MAX_NUM = 49
NUM_NUMS = 6
ticket_nums = []
for i in range(NUM_NUMS):
    rand = randrange(MIN_NUM, MAX_NUM + 1)
    while rand in ticket_nums:
        rand = randrange(MIN_NUM, MAX_NUM + 1)
    ticket_nums.append(rand)
ticket_nums.sort()
print("Номера вашего билета: ", end = "")
for n in ticket_nums:
    print(n, end = " ")
print()

#5.2.6
def isSorted(lst):
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        return True
    else:
        return False

list = []
n = int(input())
while n!=0:
    list.append(n)
    n = int(input())
print()
for i in range(len(list)):
    print(list[i], end=' ')
print()
print(isSorted(list))
