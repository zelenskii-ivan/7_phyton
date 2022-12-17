import sys

import logger
import model
import model_delete_contact
import view


def show_main_menu():
    menu_num = view.start_phonebook()

    if menu_num == '1':
        file1 = open(model.file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Телефонный справочник пуст")
        else:
            print(file_contents)
        file1.close
        ent = input("Нажмите Ввод для продолжения...")
        show_main_menu()
    elif menu_num == '2':
        logger.enter_contact_record()
        ent = input("Нажмите Ввод для продолжения...")
        show_main_menu()
    elif menu_num == '3':
        model.search_contact_record()
        ent = input("Нажмите Ввод для продолжения...")
        show_main_menu()
    elif menu_num == '4':
        model_delete_contact.delete_contact()
        ent = input("Нажмите Ввод для продолжения...")
        show_main_menu()

    elif menu_num == '5':
        print("Выход")
        sys.exit
    else:
        print("Ошибка, Введите [1 до 4]\n")
        ent = input("Нажмите Ввод для продолжения...")
        show_main_menu()