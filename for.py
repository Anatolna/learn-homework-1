"""

Домашнее задание №1

1. Цикл for: часть 1

* Создать список из десяти целых чисел.
Вывести на экран каждое число, увеличенное на 1.

* Ввести с клавиатуры строку.
Вывести эту же строку вертикально: по одному символу на строку консоли.


2. Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

list = [1, 5, 3, 40, 5, 6, 7, -8, 9, 1010]
for number in list:
    print(number + 1)

str = input('Введите строку: ')
for simb in str:
    print(simb)

school = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5b', 'scores': [2,4,5,4,3]},
    {'school_class': '3c', 'scores': [3,4,3,4,5]},
    {'school_class': '8a', 'scores': [3,3,5,4,3]}
] 

all_scores = []
for klass in school:
    all_scores += klass['scores']
print(f'Средний балл по школе: {sum(all_scores)/len(all_scores)}')  

"""
avg_by_class = {}
for each_class in school:
    print(each_class)
    print(each_class['school_class'])
    print(each_class['scores'])
    avg_by_class[each_class['school_class']] = sum(each_class['scores'])/len(each_class['scores'])
    print(avg_by_class)
"""

for each_class in school:
    print(f'Средний балл по классу: {each_class["school_class"]} {sum(each_class["scores"])/len(each_class["scores"])}')