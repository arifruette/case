import random
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np

#время необходимое чтобы дойти до каждой ячейки

b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 4, 4, 4, 4, 4, 5, 6, 7,
     8, 9, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 8, 8, 8, 8, 8, 8,
     8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

results = []
for i in range(500):
    a = [0] * 100

    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    # массивы для цветов (сколько идти до нужных ячеек)
    ss = []
    for i in range(100):
        a[i] = int(random.random() * 5) + 1  # создание таблицы с цветами
    for i in range(100):
        if a[i] == 1:
            c1.append(b[i] * 2)
        if a[i] == 2:
            c2.append(b[i] * 2)
        if a[i] == 3:
            c3.append(b[i] * 2)
        if a[i] == 4:
            c4.append(b[i] * 2)
        if a[i] == 5:
            c5.append(b[i] * 2)
    r1 = 0  # робот 1
    r2 = 0  # робот 2
    s = 0  # счётчик секунд
    u = 0  # счётчик номера в массиве
    while True:
        if r1 == 0:
            r1 = c1[u]
            u += 1
        if u > len(c1) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        if r2 == 0:
            r2 = c1[u]
            u += 1  # если робот дошел дать ему другую задачу
        if u > len(c1) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        s += 1  # прошло на секунду больше времени
        r1 -= 1
        r2 -= 1  # роботы стали на секунду ближе к цели
    ss.append(s)
    r1 = 0  # робот 1
    r2 = 0  # робот 2
    s = 0  # счётчик секунд
    u = 0  # счётчик номера в массиве
    while True:
        if r1 == 0:
            r1 = c2[u]
            u += 1
        if u > len(c2) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        if r2 == 0:
            r2 = c2[u]
            u += 1  # если робот дошел дать ему другую задачу
        if u > len(c2) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        s += 1  # прошло на секунду больше времени
        r1 -= 1
        r2 -= 1  # роботы стали на секунду ближе к цели
    ss.append(s)
    r1 = 0  # робот 1
    r2 = 0  # робот 2
    s = 0  # счётчик секунд
    u = 0  # счётчик номера в массиве
    while True:
        if r1 == 0:
            r1 = c3[u]
            u += 1
        if u > len(c3) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        if r2 == 0:
            r2 = c3[u]
            u += 1  # если робот дошел дать ему другую задачу
        if u > len(c3) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        s += 1  # прошло на секунду больше времени
        r1 -= 1
        r2 -= 1  # роботы стали на секунду ближе к цели
    ss.append(s)
    r1 = 0  # робот 1
    r2 = 0  # робот 2
    s = 0  # счётчик секунд
    u = 0  # счётчик номера в массиве
    while True:
        if r1 == 0:
            r1 = c4[u]
            u += 1
        if u > len(c4) - 1:
            s = s + max(r1, r2)  #если кончился массив дальше не продолжать
            break
        if r2 == 0:
            r2 = c4[u]
            u += 1  # если робот дошел дать ему другую задачу
        if u > len(c4) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        s += 1  # прошло на секунду больше времени
        r1 -= 1
        r2 -= 1  # роботы стали на секунду ближе к цели
    ss.append(s)
    r1 = 0  # робот 1
    r2 = 0  # робот 2
    s = 0  # счётчик секунд
    u = 0  # счётчик номера в массиве
    while True:
        if r1 == 0:
            r1 = c5[u]
            u += 1

        if u > len(c5) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        if r2 == 0:
            r2 = c5[u]
            u += 1  # если робот дошел дать ему другую задачу
        if u > len(c5) - 1:
            s = s + max(r1, r2)  # если кончился массив дальше не продолжать
            break
        s += 1  # прошло на секунду больше времени
        r1 -= 1
        r2 -= 1  # роботы стали на секунду ближе к цели
    ss.append(s)
    results.append(max(ss))


fig, ax = plt.subplots()

fig.set_figwidth(650)

ax.plot(results)
ax.xaxis.set_minor_formatter(matplotlib.ticker.FixedFormatter(range(50, 500, 100)))
locator = matplotlib.ticker.FixedLocator(range(0, 500, 50))
ax.xaxis.set_minor_locator(locator)

mean = np.mean(results)
plt.axhline(mean, color='r', linestyle='--')

plt.text(-24, np.mean(results)+3, f'{mean:.2f}', ha='left', va='center', color='black')
plt.text(0, np.max(results)-0.2, f'Максимальное значение: {np.max(results):.2f}', ha='left', va='center', color='g')
plt.text(0, np.min(results)+0.2, f'Минимальное значение: {np.min(results):.2f}', ha='left', va='center', color='b')

plt.xlabel("Номер итерации")
plt.ylabel("Время работы роботов")


plt.legend()


plt.show()