import controller

file_name = "phonebook.txt"
file1 = open(file_name, "a+")
file1.close()


def search_contact_record():
    search_name = input("Введите Имя для поиска контакта: ")

    search_name = search_name.title()
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()

    found = False
    for line in file_contents:
        if search_name in line:
            print("Ваш контакт:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("В телефонном справочнике, нет контакта с именем = " + search_name)
        controller.show_main_menu()