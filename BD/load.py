#При запуске выводится следующее сообщение: Выбирете нужный бэкап. После чего идет список всех бэкапов в столбик и они пронумерованы, когда пользователь вводит номер какого то бэкапа, то база восстанавливается по этому бэкапу
import os
import platform
print("№  Имя файла")
print("-  ---------")
n = 1
files = {}
for i in os.listdir("backups"):
    files['n']=i
    print(str(n) + '. ' + str(i))
    n += 1
answer = input('Vyberite nuzhniy backup\n')
if answer == "" or int(answer) > n-1:
    print ('Operation canceled')
else:
    if platform.platform() == "Windows":
        os.system('python manage.py flush')
        os.system(f'python manage.py loaddata backups/{files[answer]}')
    else:
        os.system('python3 manage.py flush')
        os.system(f'python3 manage.py loaddata backups/{files[answer]}')
      