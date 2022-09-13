# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

# Программа получилась как получилась=D 
# Для записи многочлена используйте все степени переменной, начиная с наибольшей
# Пример: если многочлен вида 3*(x^3) + 2*x -> 3*(x^3) + 0*(x^2) + 2*(x^1) + 0

def list_to_int(data):                       # Функция, передающая коэффициенты переменных в список
    ddd = list(data)
    string = ddd[0]
    fff = []
    for i in range(len(string)):
        if string[i] == 'x':
            fff.append(string[i-4])
            fff.append(string[i-3])
    fff.append(string[len(string)-2])
    fff.append(string[len(string)-1])

    ttt = []
    for i in range(0, len(fff), 2):
        n = fff[i] + fff[i+1]
        ttt.append(n)
    return(ttt)

data = open('1.txt', 'r')                        # Открываем файл для чтения и вызываем функцию для определения коэф.
num_list_1 = list_to_int(data)

data = open('2.txt', 'r')
num_list_2 = list_to_int(data)

if len(num_list_1) != len(num_list_2):            # Если многочлены разных степеней, то добавляем нули к списку с меньшим количеством степеней
    if len(num_list_1) > len(num_list_2):
        difference = len(num_list_1) - len(num_list_2)
        for i in range(difference):
            num_list_2.insert(0, '0')
    else:
        difference = len(num_list_2) - len(num_list_1)
        for i in range(difference):
            num_list_1.insert(0, '0')

print(num_list_1)                                # Для проверки выведем коэффициенты в терминал
print(num_list_2)

final = []
for i in range(len(num_list_1)):                 # Сложим коэффициенты в новый список final[]
    num1 = int(num_list_1[i])
    num2 = int(num_list_2[i])
    num3 = num1 + num2
    final.append(num3)
print(final)                                     # Для проверки так-же выведем список в терминал

k = len(final) - 1                               
data = open('sum.txt', 'w')                      # Запишим получившиеся коэф-ты с переменными в файл 'sum.txt'
for i in range(len(final) - 1):
    if final[i] == 0:
        k -= 1
        continue
    data.write(f'{final[i]}*(x^{k}) + ')
    k -= 1
data.write(f'{final[len(final)-1]}')
data.close() 