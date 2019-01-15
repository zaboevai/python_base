# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
i = 0
student_income = educational_grant
months_expenses = 0
money_needs = 0

while i < 10:

    if i == 0:
        months_expenses = expenses
    elif i >= 1:
        months_expenses *= 1.03
    i += 1
    diference = round(months_expenses-student_income, 2)
    money_needs += diference
    print('Расходы в', i, 'месяце:', diference, ', Итого за', i, 'мес.:', round(money_needs,2))

print('Студенту надо попросить', money_needs, 'рублей')