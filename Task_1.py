# Вычислить число c заданной точностью d

import math

def precision(pi, d):
    pi = ((pi * (10**d)) // 1) / (10**d)
    return(pi) 

d = int(input('Введите точность: '))
pi = math.pi


print(f'Число Пи с точностью {d} после запятой = {precision(pi, d)}')