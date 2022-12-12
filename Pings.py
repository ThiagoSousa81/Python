import os
import time
with open('C:/Users/Tecno Space/Documents/Cursos/DIO/File.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    print('#' * 60)
    for ip in dump:
        print('Verificando o IP: ', ip)
        print('-' * 60)
        os.system('ping -n 3 {}'.format(ip))
        print('-' * 60)
        time.sleep(2)
