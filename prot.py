# Поляков Андрей ИУ7-12Б
# sin x
# Методом трапеций от а до b с разбиением n

import math as m


def f(x):
    return m.sin(x)


def adv(x):
    return -m.cos(x)


a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
n = int(input("Введите количество разбиений: "))

sf_a = a
sect = (b - a) / n
integral = 0
prev = f(a)
while a + sect < b:
    now = f(a + sect)
    integral += (prev + now) * 0.5 * sect
    prev = now
    a += sect
i = adv(b) - adv(sf_a)

print(f"\nПриближенный интеграл: {integral:.5g}")
print(f"Интеграл: {i:.5g}")
