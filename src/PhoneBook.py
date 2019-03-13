interrupter = True
contacts = dict()


def add_user():
    name = input("Введите Имя\n")
    number = input("Введите Номер\n")
    contacts[name] = number


def get_number():
    name = input("Введите имя для поиска\n")
    print(contacts.get(name))


def delete_user():
    name = input("Введите имя для удаления\n")
    contacts.__delitem__(name)


def print_list():
    print(contacts)


while interrupter:
    command = input("Введите команду: 1 - Добавить контакт, 2 - Вернуть номер по имени, 3 - Удалить человека по имени, 4 - Вывод списка, 0 - Выход\n")
    if command == "1":
        add_user()
    elif command == "2":
        get_number()
    elif command == "3":
        delete_user()
    elif command == "4":
        print_list()
    elif command == "0":
        print("Работа завершена запросу")
        interrupter = False
    else:
        print("Работа завершена по неверному вводу")
        interrupter = False
