"""
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

str1 = b'class'
str2 = b'function'
str3 = b'method'

lst1 = [str1, str2, str3]

for i in lst1:
    print(f'содержимое - {i}, тип - {type(i)}, длина - {len(i)}')