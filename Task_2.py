# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

import math


def prost(n):
    ddd = []
    i = 2
    while ((i**2) <= n):
        if ((n % i) == 0):
            ddd.append(i)
            n //= i
        else :
            i += 1 
    if n > 1:
        ddd.append(n)     
    return(ddd)

n = int(input('N = '))
print(prost(n))