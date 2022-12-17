import controller
from model import file_name


def delete_contact():
    search_name = input("Введите Имя для поиска и удаления контакта: ")

    search_name = search_name.title()
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()

    found = False
    for line in file_contents:
        if search_name in line:
            print("Ваш контакт:", end=" ")
            print(line)
            found = True
            file = open('phonebook.txt', "r")
            f = file.read().replace(line, '')
            file2 = open('phonebook.txt', 'w')
            file2.write(f)
            file2.close()
            break
    if found == False:
        print("В телефонном справочнике, нет контакта с именем = " + search_name)
        controller.show_main_menu()