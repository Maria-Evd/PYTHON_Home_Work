
# сделать консольное приложение Телефонный справочник 
# с внешним хранилищем информации, и чтоб был реализован
# основной функционал - просмотр, сохранение, 
# импорт, поиск, удаление, изменение данных

import json

data = {}

def load_data():
    with open("contacts.json", "r", encoding = "utf-8") as fh:
        data = json.load(fh)
    print("Телефонная книга была успешно загружена в файл contacts.json ")
   

def save_data():
    with open("contacts.json", "w", encoding = "utf-8") as fh:
        fh.write(json.dumps(data, ensure_ascii=False))
    print("Телефонная книга была обновлена")
       

data = {'Иванов Степан':{'phones':['89526756453','85645789765'], 'BD': '23.07.1994', 'email': 'stepash@mail.ru'}, 'Степанов Иван':{'phones':['893456789213'], 'BD': '01.01.1990', 'email': 'ivash@mail.ru'}}


while True:
    command=input("Введите команду ")
    if command == "/start":
        print ("Вы открыли телефонную книгу, добро пожаловать! ")
    elif command == "/stop":
        save_data()
        print ("Вы закрыли телефонную книги, до скорой встречи! ")
        break
    elif command == "/find":
        find_name = input("Введите имя контакта ")
        if find_name in data:
            print(data[find_name])
        else:
            print("Такого контакта не существует!")   
    elif command == "/all":
        print ("Текущий список контактов ")
        for key, value in data.items():
            print(f"{key} - {value}")
    elif command == "/add":
        name = input("Введите имя нового контакта ")
        if name in data:
            print("Такой контакт существует! Назовите его иначе!")
        else:
            coll = int(input("Введите количество номеров контакта "))
            numbers = []
            for i in range(coll):
                num = input(f"Введите {i+1} номер контакта ")
                numbers.append(num)
            day = input("Введите день рождения контакта ")
            mail = input("Введите адрес электронной почты контакта ")
            data[name] = {'phones': numbers, 'BD': day, 'email': mail}
            print("Контакт успешно добавлен в телефонную книгу!")
        
    elif command == "/help":
        print("Основные команды телефонной книги: ") # добавим чуть позже
    elif command == "/delete":
        f = input("Введите имя контакта, который надо удалить ")
        if f in data:
            del data[f]
            print("Контакт успешно удален!")
        else:
            print("Такого контакта нет в телефонной книге")
    elif command == "/save":
        save_data()  
    elif command == "/load": 
        load_data()    
    else:
        print ("Неопознанная команда. Просьба изучить мануал через /help ")
        