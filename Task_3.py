# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def correct(ddd):
    fff = []
    for i in range(len(ddd)):
        if ddd[i] not in fff:
            fff.append(ddd[i])
    return(fff)

ddd = [1, 2, 2, 7, 3, 4, 5, 5, 7, 7, 7]
print(correct(ddd))

# Попробовал сделать c помощью удаления из списка элемента, 
# но из-за сдвига после удаления программа пропускает один элемент, а он может быть такойже

# ddd = [1, 2, 2, 7, 3, 4, 5, 5, 7, 7, 7]
# i = 0
# while i < (len(ddd)):
#     j = i + 1 
#     while j < (len(ddd)):
#         if (ddd[i] == ddd[j]):
#             del ddd[j]
#         j += 1
#     i += 1

# print(ddd)