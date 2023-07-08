import os
import subprocess
import psutil
import time


PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        # catalog = os.getcwd()
        # p = f'"python", {catalog}/server.py'
        PROCESS.append(subprocess.Popen(['python', 'server.py']))

        time.sleep(0.1)
        for i in range(1,2):
            # p = f'python {catalog}/client.py -m send -u userS{i}'
            PROCESS.append(subprocess.Popen(['python', 'client.py -n User1']))
            # print(p)
            time.sleep(0.1)
        # for i in range(1, 2):
        #     # p = f'python {catalog}/client.py -m listen -u userL{i}'
        #     PROCESS.append(subprocess.Popen(["gnome-terminal", "--", "sh", "-c", p]))
        #     # print(p)
        #     time.sleep(0.1)
    elif ACTION == 'x':
        while PROCESS:
            PROCESS.pop().kill()
