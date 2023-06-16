# Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.

def num_translate(key):
    x = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'черыре',
         'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
         'nine': 'девять', 'ten': 'десять'}
    return x.get(key)