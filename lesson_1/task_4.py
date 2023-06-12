"""
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
"""

lst1 = ['разработка', 'администрирование', 'protocol', 'standard']
lst_bytes = []
lst_decode =[]

for i in lst1:
    lst_bytes.append(i.encode('utf-8'))

for j in lst_bytes:
    lst_decode.append(j.decode('utf-8'))

print(f'слова в байтовом представлении - \n{lst_bytes}')
print(f'обратное преобразование - \n{lst_decode}')