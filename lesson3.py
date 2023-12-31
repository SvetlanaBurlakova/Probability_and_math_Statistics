import math
import numpy as np
def combinations(k,n):
     return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
"""Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 
75, 65, 84, 90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной 
выборки."""

arr = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

arr_mean = sum(arr)/len(arr)
print(f'Среднее арифметическое выборки = {arr_mean}')
var = sum([pow(a - arr_mean, 2) for a in arr])/len(arr)
print(f'Смещенная дисперсия ={var:.2f}')
print(f'Несмещенная дисперсия = {sum([pow(a - arr_mean, 2) for a in arr])/(len(arr)-1):.2f}')
print(f'Среднее квадратичное отклонение = {math.sqrt(var):.2f}')

"""2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, 
что 3 мяча белые?"""

"""Возможные варианты:
1. из первого ящика 2 белых 0 черных, из второго 1 белый 3 черных
2. из первого ящика 1 белый 1 черный, из второго 2 белых 2 черных
3. из первого 0 белых 2 черных, из второго 3 белых 1 черный"""

prob1 = combinations(2, 5) * combinations(0, 3)/combinations(2, 8) * \
        combinations(1, 5) * combinations(3, 7)/ combinations(4, 12)

prob2 = combinations(1, 5) * combinations(1, 3)/combinations(2, 8) * \
        combinations(2, 5) * combinations(2, 7)/ combinations(4, 12)

prob3 = combinations(0, 5) * combinations(2, 3)/combinations(2, 8) * \
        combinations(3, 5) * combinations(1, 7)/ combinations(4, 12)

print(f'Вероятность вытащить 3 белых мяча = {prob1 + prob2 + prob3:.2f}')

"""3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). 
третьим спортсменом."""
p1 = 0.9
p2 = 0.8
p3 = 0.6
p_full = p1 + p2 + p3
print(f'Вероятность что попал первый спортсмен = {p1/p_full:.2f}')
print(f'Вероятность что попал второй спортсмен = {p2/p_full:.2f}')
print(f'Вероятность что попал третий спортсмен = {p3/p_full:.2f}')

"""4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов 
поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую 
сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). 
на факультете C?"""

p1 = 0.8 * 0.25
p2 = 0.7 * 0.25
p3 = 0.9 * 0.5
prob = p1 + p2 + p3
print(f'Вероятность того, что студент учится на факультете А = {p1/prob:.2f}')
print(f'Вероятность того, что студент учится на факультете B = {p2/prob:.2f}')
print(f'Вероятность того, что студент учится на факультете C = {p3/prob:.2f}')

"""5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: 
а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?"""

p1 = 0.1
p2 = 0.2
p3 = 0.25
prob_1 = p1 * p2 * p3

print(f'Вероятность. что в первый месяц выйдут из строя все детали =  {prob_1:.3f}')

#Вероятность того, что выйдкт из строя ровно 2 детали:
prob_2 = p1 * p2 * (1-p3) + p1 * (1-p2) * p3 + (1-p1) * p2 * p3
print(f'Вероятность. что в первый месяц выйдут из строя 2 детали =  {prob_2:.2f}')

# Веротяность того, что выйдет из строя хотя бы одна деталь = 1 - вероятность того, что ни одна деталь на выйдет из строя
prob_3 = 1 - (1 - p1) * (1 - p2) * (1 - p3)
print(f'Вероятность. что в первый месяц выйдет из строя хотя бы 1 деталь {prob_3:.2f} ')

#Вероятность того, что выйдет 1 деталь из строя равна:
prob_4 = (1-p1) * p2 * (1-p3) + p1 * (1-p2) * (1-p3) + (1-p1) * (1-p2) * p3
print(f'Вероятность. что в первый месяц выйдет из строя от 1 до 2 деталей {prob_2 + prob_4:.2f} ')