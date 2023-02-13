import pathlib
import os
from os import name as osname
import time


#Меню программы
def menu_programm():
    if answer == '1':
        get_files()
    elif answer == '2':
        create_file()
    elif answer == '3':
        create_folder()
    elif answer == '4':
        choose_file()
    elif answer == '5':
        choose_folder()
    elif answer == '6':
        delete_file()
    elif answer == '7':
        delete_folder()
    elif answer == '8':
        exit()
    else:
        print('Неизвестная команда. Подождите...')
        time.sleep(2)
        clear()
        menu_programm()
CHOOSE_ACTION = '''
Выберите действие:
1. Показать содержимое
2. Создать файл
3. Создать папку
4. Выбрать файл
5. Выбрать папку
6. Удалить файл
7. Удалить папку
8. Завершение программы
'''

CHOOSE_ACTION_FOLDER = '''
Выберите действие:
1. Показать содержимое
2. Создать файл
3. Создать папку
4. Выбрать файл
5. Выбрать папку
6. Удалить файл
7. Удалить папку
8. Завершение программы'
'''


CHOOSE_ACTION_FILE = '''
Выберите действие:
1. Чтение
2. Запись
3. Перезапись
4. Назад
'''


# Меню программы
def menu_program():
    print(CHOOSE_ACTION)

    answer = input('> ')

    match answer:
        case '1':
            get_files()
        case '2':
            create_file()
        case '3':
            create_folder()
        case '4':
            choose_file()
        case '5':
            choose_folder()
        case '6':
            delete_file()
        case '7':
            delete_folder()
        case '8':
            exit()
        case _:
            print('Неизвестная команда. Подождите...')
            time.sleep(2)
            clear()
            menu_program()


# Меню папки
def menu_folder():
    if answer == '1':
        get_files()
    elif answer == '2':
        create_file()
    elif answer == '3':
        create_folder()
    elif answer == '4':
        choose_file()
    elif answer == '5':
        choose_folder()
    elif answer == '6':
        delete_file()
    elif answer == '7':
        delete_folder()
    elif answer == '8':
        exit()
    else:
        print('Неизвестная команда. Подождите...')
        time.sleep(2)
        clear()
        menu_programm()
    print(CHOOSE_ACTION_FOLDER)

    answer = input('> ')

# Меню файла
def menu_file(name):
    print(CHOOSE_ACTION_FILE)

    answer = input('> ')

    if answer == '1':
        read_file(name)
    if answer == '2':
        write_file(name)
    if answer == '3':
        addwrite_file(name)
    if answer == '4':
        close_file(name)


# Вывести на экран содержимое папки
def get_files():
    currentDirectory = pathlib.Path('.')
    for currentFile in currentDirectory.iterdir():
        print(currentFile)

    print()
    menu_program()


# Создать файл
def create_file():
    name = input('Введите название файла: ')
    file = open(name, 'tw', encoding = 'utf-8')
    file.close()
    print('Файл успешно создан!\n')
    print()
    menu_program()


# Создать новую папку
def create_folder():
    name = input('Введиет название папки: ')
    os.mkdir(name)
    clear()
    menu_program()


# Выбрать файл
def choose_file():
    name = input('Введите имя файла: ')
    clear()
    menu_file(name)


# Выбрать папку
def choose_folder():
    name = input('Введите имя папкпи: ')
    os.chdir(name)
    clear()
    menu_folder()


# Чтение файла
def read_file(name):
    file = open(name, 'r', encoding='utf-8')
    i = 1
    for line in file:
        print(i, ' ', line, end='')
        i += 1

    file.close()
    print()
    menu_file(name)


# Чтение только что созданного файла
def read_new_file(name):
    file = open(name, 'r', encoding='utf-8')
    i = 1
    for line in file:
        print(i, ' ', line, end = '')
        i += 1

    file.close()


# Перезапись файла
def write_file(name):
    print('Введите текст. Enter -> переход на новую строку. Ctrl+C -> сохранить файл')
    text = []
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            break
        text.append(line)

    file = open(name, 'w', encoding='utf-8')
    for line in text:
        file.write(line + '\n')
    file.close()
    clear()
    print('Файл успешно записан! Содержимое файла ', name)
    read_new_file(name)


# Дописывание файла
    print('Введите текст. Enter -> переход на новую строку. Ctrl+C -> сохранить файл')
def append_to_file(name):
    text = []
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            break
        text.append(line)

    file = open(name, 'a', encoding='utf-8')
    for line in text:
        file.write(line + '\n')
    file.close()
    clear()
    print('Файл успешно записан! Содержимое файла ', name)
    read_new_file(name)


# Удалить файл
def delete_file():
    name = input('Введине имя файла: ')
    os.remove(name)
    clear()
    menu_program()


# Удалить папку
def delete_folder():
    name = input('Введите имя папки: ')
    os.rmdir(name)
    clear()
    menu_program()


# Закрыть файл
def close_file():
    clear()
    menu_program()


# Очистить консоль
def clear():
    # clear last STDOUT Windows
    if osname == "nt":
        os.system('cls')
    # linux or MacOS
    else:
        os.system('clear')


if __name__ == '__main__':
    username = input('Введите ваше имя: ')
    print('Добро пожаловать, ', username)
    menu_program()
