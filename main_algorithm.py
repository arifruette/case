import matplotlib.ticker
import numpy as np
import matplotlib.pyplot as plt

def recalc(items):
    #переменные для поиска первого и второго максимума
    maximum_1 = -10000
    ind_1 = 0
    maximum_2 = -1000001
    ind_2 = 0

    #поиск максимумов
    for i in range(len(items)):
        if items[i] >= maximum_1:
            maximum_1 = items[i]
            ind_1 = i
    for i in range(len(items)):
        if items[i] >= maximum_2 and items[i] <= maximum_1 and i != ind_1:
            maximum_2 = items[i]
            ind_2 = i
    items[ind_1] /= 2
    items[ind_2] /= 2

    # максимальный вес в идеале должен быть равен половине суммы всех времен(каждый робот будет ездить +- одно время)
    W = int(items.sum() / 2)
    n = len(items)
    dp = [0 for _ in range(W + 1)]

    for i in range(n):
        for w in range(W, 0, -1):
            if items[i] <= w:
                dp[w] = max(dp[w], dp[w - items[i]] + items[i])
    return dp[W]

results = list()
for i in range(500):
    lst = np.random.randint(1, 6, size=(10, 10))
    a, b, c, d, e = np.zeros((10, 10), dtype=int),\
    np.zeros((10, 10), dtype=int),\
    np.zeros((10, 10), dtype=int),\
    np.zeros((10, 10), dtype=int),\
    np.zeros((10, 10), dtype=int)
    categories = [a, b, c, d, e]

    for i in range(10):
        for j in range(10):
            current = categories[lst[i, j] - 1]
            current[i, j] = (max(i, j)) * 2
    result = max([recalc(i.flatten()) for i in categories])
    results.append(result)


fig, ax = plt.subplots()

fig.set_figwidth(650)

ax.plot(results)
ax.xaxis.set_minor_formatter(matplotlib.ticker.FixedFormatter(range(50, 500, 100)))
locator = matplotlib.ticker.FixedLocator(range(0, 500, 50))
ax.xaxis.set_minor_locator(locator)

mean = np.mean(results)
plt.axhline(mean, color='r', linestyle='--')

plt.text(-23, np.mean(results)+3, f'{mean:.2f}', ha='left', va='center', color='black')
plt.text(0, np.max(results)-0.2, f'Максимальное значение: {np.max(results):.2f}', ha='left', va='center', color='g')
plt.text(0, np.min(results)+0.2, f'Минимальное значение: {np.min(results):.2f}', ha='left', va='center', color='b')

plt.xlabel("Номер итерации")
plt.ylabel("Время работы роботов")

plt.legend()


plt.show()