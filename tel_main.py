# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# DZ_8 - Дополнить справочник возможностью копирования данных
# из одного файла в другой. Пользователь вводит номер строки, 
# которую необходимо перенести из одного файла в другой.

from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phones.csv'

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt
        
def get_info():
    first_name = None
    is_valid_name = False
    last_name = 'Иванов'
    phone_number = None
    is_valid_phone = False
    
    while not is_valid_name:
        first_name = input('Введите имя: ')

        if len(first_name) < 2:
            print('Вы не ввели имя')
        else:
            is_valid_name = True

    while not is_valid_phone:
        try:
        # phone_number = int(input('Введите номер: '))
            phone_number = 99999999999
            if len(str(phone_number)) != 11:
                raise LenNumberError('Не верная длина номера')
            else:
                is_valid_phone = True
        except ValueError:
            print('Не валидный номер')
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def write_file(lst):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)

    for el in res:
        if el['Телефон'] == str(lst[2]):
            print('Такой телефон уже есть в справочнике')
            return

    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}

    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        res.append(obj)
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def main():
    while True:
        command = input('Введите команду: ')

        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует')
                continue
            print(*read_file(file_name))

main()