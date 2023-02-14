import pathlib
import os
from os import name as osname
import time
from git import Repo


GIT_DIR = 'pce_git_client'

DEF_IN_TEXT_MESSAGE = "Введите текст. Enter - переход на новую строку. Ctrl+C - сохранить файл."

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
    print(CHOOSE_ACTION_FOLDER)

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


# Меню файла.
def menu_file(name: str) -> None:
    print(CHOOSE_ACTION_FILE)

    answer = input('> ')

    match answer:
        case '1':
            read_file(name)
        case '2':
            append_to_file(name)
        case '3':
            write_file(name)
        case '4':
            close_file()
        case _:
            menu_file(name)


# Вывести на экран содержимое папки
def get_files():
    path = f'./{GIT_DIR}'
    currentDirectory = pathlib.Path(path)
    for currentFile in currentDirectory.iterdir():
        print(currentFile)

    print()
    menu_program()


# Создать файл
def create_file():
    name = input('Введите название файла: ')

    path = f'./{GIT_DIR}/{name}'

    file = open(path, 'tw', encoding='utf-8')
    file.close()
    git_commit(name, 'Create')
    print('Файл успешно создан!\n')
    print()
    menu_program()


# Создать новую папку
def create_folder():
    name = input('Введите название папки: ')
    path = f'./{GIT_DIR}/{name}'
    os.mkdir(path)
    clear()
    menu_program()


# Выбрать файл
def choose_file():
    name = str(input('Введите имя файла: '))
    clear()
    menu_file(name)


# Выбрать папку
def choose_folder():
    name = input('Введите имя папки: ')
    path = f'./{GIT_DIR}/{name}'
    os.chdir(path)
    clear()
    menu_folder()


# Чтение файла
def read_file(name):
    path = f'./{GIT_DIR}/{name}'

    file = open(path, 'r', encoding='utf-8')
    i = 1
    for line in file:
        print(i, ' ', line, end='')
        i += 1

    file.close()
    print()
    menu_file(name)


# Чтение только что созданного файла
def read_new_file(name):
    path = f'./{GIT_DIR}/{name}'

    file = open(path, 'r', encoding='utf-8')
    i = 1
    for line in file:
        print(i, ' ', line, end='')
        i += 1

    file.close()


# Перезапись файла
def write_file(name):
    clear()
    print(DEF_IN_TEXT_MESSAGE)
    text = []
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            break
        text.append(line)

    path = f'./{GIT_DIR}/{name}'

    file = open(path, 'w', encoding='utf-8')
    for line in text:
        file.write(line + '\n')
    file.close()
    git_commit(name, 'Write into')
    clear()
    print('Файл успешно записан! Содержимое файла ', name)
    read_new_file(name)


# Дописывание файла
def append_to_file(name):
    clear()
    print(DEF_IN_TEXT_MESSAGE)
    text = []
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            break
        text.append(line)

    path = f'./{GIT_DIR}/{name}'

    file = open(path, 'a', encoding='utf-8')
    for line in text:
        file.write(line + '\n')
    file.close()
    git_commit(name, 'Append into')
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


def git_commit(name: str, info: str):
    root = f'./{GIT_DIR}/'

    if not os.path.exists(root[:-1]):
        os.mkdir(f'./{GIT_DIR}')
        Repo.init(path=root)
    elif not os.path.exists(f'{root}.git'):
        Repo.init(path=root)

    repo = Repo(root)

    repo.index.add(items=[name])
    repo.index.commit(f'{info} {name}')

    repo.close()

    return None


if __name__ == '__main__':
    username = input('Введите ваше имя: ')
    print('Добро пожаловать, ', username)
    menu_program()
