from scipy import stats

"""
1 )  Даны две  независимые выборки. Не соблюдается условие нормальности
x1  380,420, 290
y1 140,360,200,900

Сделайте вывод по результатам, полученным с помощью функции
"""

arr1 = [380,420, 290]
arr2 = [140,360,200,900]

print(stats.mannwhitneyu(arr1,arr2))
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286

# pvalue = 0.63 > 0.05,Т.О. Принимаем нулевую гипотезу, 0 том, что статистической значимых различий в этих выборках нет.

"""
2 ) Исследовалось влияние препарата на уровень давления пациентов. 
Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. 
Есть ли статистически значимые различия?

1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150,  130, 135
3е измерение через 30 минут: 130, 130, 120, 130, 125
"""

sample1 = [150, 160, 165, 145, 155]
sample2 = [140, 155, 150,  130, 135]
sample3 = [130, 130, 120, 130, 125]

print(stats.friedmanchisquare(sample1, sample2, sample3))
# FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)

# pvalue = 0.008 < 0.05,Т.О. Принимается альтернативная гипотеза, о то. что существуют статистически значимые различия в выборках,
# то есть препарат оказывает эффект на пациаентах.

"""
3 ) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
"""
print(stats.wilcoxon(sample1, sample2))
# WilcoxonResult(statistic=0.0, pvalue=0.0625)

# pvalue = 0.0625 > 0.05,Т.О. Принимаем нулевую гипотезу, 0 том, что статистической значимых различий
# в этих выборках нет. То есть влияние препарата на на пациентов нет.

"""
4) Даны 3 группы  учеников плавания.
В 1 группе время на дистанцию 50 м составляют:
56, 60, 62, 55, 71, 67, 59, 58, 64, 67

Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
"""
gr1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
gr2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
gr3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]

print(stats.kruskal(gr1, gr2, gr3))
# KruskalResult(statistic=5.465564058257224, pvalue=0.06503809985904942)

# pvalue = 0.065 > 0.05,Т.О. Принимаем нулевую гипотезу, 0 том, что статистически значемых различий нет в том,
# как плаваю ученики в разных группах

"""
5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см. 
Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. 
Объем выборки 10, уровень статистической значимости 5%

2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
"""
mean_pop = 2.5
arr = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
mean_sample = sum(arr)/len(arr)
print(f'Среднее значение выборки = {mean_sample = :.2f}') # = 2.53
dispersion = sum([(a - mean_sample)**2 for a in arr])/(len(arr) - 1)
sigma = pow(dispersion, 0.5)
print(f'Среднеквадротичное отклонение выборки = {sigma:.2f}') # = 0.16
t_r = (mean_sample - mean_pop)/(sigma/(len(arr) ** 0.5))
print(f'Расчетное значение t-критерия {t_r:.3f}') # 0.563
# при таком значении t-критерия табличное = 1.88, что значительно больше расчетного.
# То есть мы принимаем нулевую гипотезу.

# Проверка
print(stats.ttest_1samp(arr, mean_pop))
# TtestResult(statistic=0.5630613661802959, pvalue=0.5871439993940629, df=9)