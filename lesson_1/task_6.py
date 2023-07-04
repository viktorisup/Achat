"""
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect
from chardet.universaldetector import UniversalDetector

with open('test_file.txt', 'rb') as f:
    text = f.read()

print(detect(text))

with open('test_file.txt', 'r', encoding='utf-8') as f:
    print(f.read())
