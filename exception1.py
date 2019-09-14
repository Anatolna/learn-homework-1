"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
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
        try:
            user_say = input('Спросите что-нибудь: ')
            print(dictt[user_say])
        except KeyError:
            print(f'Я не понял, что значит {user_say}')
        except KeyboardInterrupt:
            print(' - Пока!')
            break
        
if __name__ == "__main__":
    ask_user()
