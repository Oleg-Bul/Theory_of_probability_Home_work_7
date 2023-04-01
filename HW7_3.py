import numpy as np
import scipy.stats as stats


# Исследовалось влияние препарата на уровень давления пациентов.
# Сначала измерялось давление до приема препарата,
#  потом через 10 минут и через 30 минут.
# Есть ли статистически значимые различия?

# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150,  130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125


# Сравните 1 и 2 е измерения, предполагая,
# что 3го измерения через 30 минут не было.

alpha = 0.05
x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
d = stats.wilcoxon(x1, x2)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.wilcoxon(x1, x2)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза не \
отвергается, препарат не влияет на давление.')
else:
    print('>>> Cтатистически значимые различия присутствуют,\
нулевую гипотезу отвергаем, препарат влияет на давление.')
