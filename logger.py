import controller
from model import file_name


def enter_contact_record():
    first = input('Введите Имя: ')
    first = first.title()
    last = input('Введите Фамилию: ')
    last = last.title()
    phone = input('Введите телефонный номер: ')
    email = input('Введите E-mail: ')
    contact = ("[" + first + " " + last + ", " + phone + ", " + email + "]\n")
    file1 = open(file_name, "a+")
    file1.write(contact)
    file1.close()
    print("Контакт\n " + contact + "успешно добавлен!")
    controller.show_main_menu()