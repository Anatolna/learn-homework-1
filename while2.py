"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    dictt = {
        'Как дела?': 'Хорошо!', 
        'Что делаешь?': 'Программирую',
        'Пойдем гулять?': 'Не могу',
        'Когда сможешь?': 'Завтра'
    }
    dictt['Уже все?'] = 'Еще нет'
    while True:
        user_say = input('Спросите что-нибудь: ')
        try:
            print(dictt[user_say])
        except KeyError:
            print(f'Я не понял, что значит {user_say}')
        
if __name__ == "__main__":
    ask_user()
