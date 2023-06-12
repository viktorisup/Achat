"""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных
выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения
данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить
в виде списка и поместить в файл main_data (также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
"""

import re
import csv
import os


os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = []
def get_data():
    for root, dirs, files in os.walk('./'):
        file_lst = files
        for i in file_lst:
            if '.txt' in i:
                with open(f'{i}', 'r', encoding='utf-8') as file_obj:
                    data_obj = file_obj.read()
                    os_prod_reg = re.findall('Изготовитель системы:\s*\S*', data_obj)
                    os_prod_list.append(os_prod_reg[0].split()[-1])
                    os_name_reg = re.findall('Название ОС:\s*\S*', data_obj)
                    os_name_list.append(os_name_reg[0].split()[-1])
                    os_code_reg = re.findall('Код продукта:\s*\S*', data_obj)
                    os_code_list.append(os_code_reg[0].split()[-1])
                    os_type_reg = re.findall('Тип системы:\s*\S*', data_obj)
                    os_type_list.append(os_type_reg[0].split()[-1])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    for el in range(len(os_prod_list)):
        row_data = []
        row_data.append(el+1)
        row_data.append(os_prod_list[el])
        row_data.append(os_name_list[el])
        row_data.append(os_code_list[el])
        row_data.append(os_type_list[el])
        main_data.append(row_data)
    return main_data


def write_to_csv(out_file):
    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data_report.csv')



