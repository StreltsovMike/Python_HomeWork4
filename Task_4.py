# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

from random import randint


k = int(input('k = '))
kkk = []
for i in range(k+1):
    kkk.append(randint(0, 100))

data = open('file.txt', 'w')
for i in range(k):
    if kkk[i] == 0:
        k -= 1
        continue
    data.write(f'{kkk[i]}*(x^{k}) + ')
    k -= 1
data.write(f'{kkk[k+1]} = 0')
data.close()