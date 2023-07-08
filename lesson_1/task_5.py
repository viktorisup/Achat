"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess
import chardet


ya_args = ['ping', 'yandex.ru']
yt_args = ['ping', 'youtube.com']
ya_ping = subprocess.Popen(ya_args, stdout=subprocess.PIPE)
yt_ping = subprocess.Popen(yt_args, stdout=subprocess.PIPE)

for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))