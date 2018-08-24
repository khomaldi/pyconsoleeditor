import pathlib
import os
import time


#Меню программы
def menu_programm():
    print('Выберите действие:\n1.Показать содержимое\n2.Создать файл\n3.Создать папку\n4.Выбрать файл\n5.Выбрать папку\n6.Завершение программы\n')
    answer = input('-->')
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
        exit()
    else:
        print('Неизвестная команда. Подождите...')
        time.sleep(2)
        clear()
        menu_programm()

#Меню папки
def menu_folder():
    answer = input(
        'Выберите действие:\n1.Показать содержимое\n2.Создать файл\n3.Создать папку\n4.Выбрать файл\n5.Выбрать папку\n6.Завершение программы')
    if answer == 1:
        get_files()
    if answer == 2:
        create_file()
    if answer == 3:
        create_folder()
    if answer == 4:
        choose_file()
    if answer == 5:
        choose_folder()

#Меню файла
def menu_file(name):
    print('Выберите действие:\n1.Чтение\n2.Запись\n3.Перезапись\n4.Закрыть файл')
    answer = input('-->')
    if answer == '1':
        read_file(name)
    if answer == '2':
        write_file(name)
    if answer == '3':
        addwrite_file(name)
    if answer == '4':
        close_file(name)

#Вывести на экран содержимое папки
def get_files():
    currentDirectory = pathlib.Path('.')
    for currentFile in currentDirectory.iterdir():
        print(currentFile)

    print()
    menu_programm()

#Создать файл
def create_file():
    name = input('Введите название файла: ')
    file = open(name, 'tw', encoding='utf-8')
    file.close()
    print('Файл успешно создан! Подождите... \n')
    time.sleep(2)
    menu_programm()

#Создать новую папку
def create_folder(foldersName):
    os.mkdir(foldersName)

#Выбрать файл
def choose_file():
    name = input('Введите имя файла: ')
    menu_file(name)
    clear()

def choose_folder():
    name = input('Введите имя папкпи: ')
    menu_folder()
    clear()

#Чтение файла
def read_file():
    name = input('Введите имя файла: ')
    file = open(name, 'r')
    for line in file:
        print(line, end = '')
        file.close()

#Чтение только что созданного файла
def read_new_file(name):
    file = open(name, 'r')
    for line in file:
        print(line, end = '')
        file.close()

#Перезапись файла
def write_file(name):
    file = open(name, 'w')
    text = input('--> ')
    file.write(text)
    print('Файл успешно записан! Подождите...')
    time.sleep(2)
    clear()
    read_new_file(name)

#Дописывание файла
def addwrite_file(name):
    file = open(name, 'a')

#Удалить папку
def delete_folder(foldersName):
    os.rmdir(foldersName)

#Закрыть файл
def close_file(name):
    name.close()

#Очистить консоль
def clear():
    os.system('cls')

username = input('Введите ваше имя: ')
print('Добро пожаловать, ', username)
menu_programm()


