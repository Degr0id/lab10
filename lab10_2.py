# Поляков Андрей ИУ7-12Б
#
# Программа для вычисления приближённого значения интеграла
# известной, заданной в программе, функции методами левых прямоугольников и 3/8

import math as m


def func(x):  # Заданная функция
    return m.sin(x)


def antiderivetive(x):  # Первообразная
    return -m.cos(x) + 4


def l_rect_method(start, end, num, f):  # Метод левых прямоугольников
    sect = (end - start) / num
    integr = 0
    x = start
    while x < end:
        integr += sect * f(x)
        x += sect
    return integr


def three_eight_method_alt(start, end, num, f):
    sect = (end - start) / num
    a = start
    integr = 0
    b = a + sect
    while b <= end:
        smm = 0
        for cnt in range(4):
            if cnt == 0:
                smm += f(a)
            elif cnt == 3:
                smm += f(b)
            else:
                smm += 3 * f(a)
            a += sect / 3
        integr += (sect / 8) * smm
        a, b = b, b + sect
    return integr


def table(n_1, n_2, arr):  # Построение таблиц
    dash = "-"
    l_i1 = f"{arr[0]:.7g}"
    l_i2 = f"{arr[1]:.7g}"
    l_i3 = f"{arr[2]:.7g}"
    l_i4 = f"{arr[3]:.7g}"
    m_length = max(len(l_i1), len(l_i2), len(l_i3), len(l_i4))
    print(f"Кол-во участков разбиения | {str(n_1).center(m_length)} | {str(n_2).center(m_length)}\n{dash * 55}")
    print(f"Метод левых прямоуг.      | {l_i1.center(m_length)} | {l_i2.center(m_length)}\n{dash * 55}")
    print(f"3/8                       | {l_i3.center(m_length)} | {l_i4.center(m_length)}\n{dash * 55}")


while True:
    try:
        st = float(input("Начало отрезка интегрирования: "))  # Ввод данных и проверка
        ed = float(input("Конец отрезка интегрирования: "))
        n1 = int(input("Количество участков разбиения N1: "))
        n2 = int(input("Количество участков разбиения N2: "))
    except ValueError:
        print("Количество участков должно быть целым числом\n")
    else:
        if st > ed:
            print("Начало не может быть больше конца\n")
        elif n1 <= 0 or n2 <= 0:
            print("Количество участков должно быть больше нуля\n")
        else:
            break

integrals = [l_rect_method(st, ed, n1, func),
             l_rect_method(st, ed, n2, func),  # Вычисление приблиз. знач. интеграла
             three_eight_method_alt(st, ed, n1, func),
             three_eight_method_alt(st, ed, n2, func)]
tru_integral = antiderivetive(ed) - antiderivetive(st)  # Вычисление интеграла
abs_delts = []
for it in integrals:
    temp = it - tru_integral
    abs_delts.append(temp)  # Абсолютные погрешности
relative_delts = []
for it in abs_delts:
    r_dlt = abs(it / tru_integral * 100) if tru_integral != 0 else '-'
    relative_delts.append(r_dlt)  # Относительные погрешности

print(f"Интеграл: {tru_integral}")
print("\nПриближенные значения интеграла:")  # Вывод
table(n1, n2, integrals)
print("\nАбсолютные погрешности:")
table(n1, n2, abs_delts)
print("\nОтносительные погрешности (в процентах):")
if tru_integral == 0:
    print("Нельзя вычислить, так как интеграл равен нулю")
table(n1, n2, relative_delts)

i_less_accurate = 0
min_acc = abs(abs_delts[0])
for i in range(4):
    if relative_delts[i] and abs(relative_delts[i]) < min_acc:
        min_acc = abs(relative_delts[i])
        i_less_accurate = i
del min_acc
while True:
    try:
        EPS = float(input("\nВведите точность: "))
        limit = int(input("Введите максимальное количество итераций: "))
    except ValueError:
        print("Введите число")
    else:
        break
if i_less_accurate >= 2:  # Перебор
    n = 1
    prev = l_rect_method(st, ed, n, func)
    while n < limit:
        now = l_rect_method(st, ed, n * 2, func)
        if abs(prev - now) < EPS:
            break
        prev = now
        n *= 2
else:
    n = 1
    prev = three_eight_method_alt(st, ed, n, func)
    while n < limit:
        now = three_eight_method_alt(st, ed, n * 2, func)
        if abs(prev - now) < EPS:
            break
        prev = now
        n *= 2

if n >= limit:
    print("Точности не удалось достичь")
else:
    print(f"Необходимое для I{i_less_accurate + 1} количество участков разбиения: {n}")