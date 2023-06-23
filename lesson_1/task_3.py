"""
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''.
"""

str1 = 'attribute'
str2 = 'класс'
str3 = 'функция'
str4 = 'type'

lst1 = [str1, str2, str3, str4]

for i in lst1:
    try:
        print(bytes(i, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{i}" невозможно записать в виде байтовой строки')
