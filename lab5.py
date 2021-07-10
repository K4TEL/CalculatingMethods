import matplotlib.pyplot as plt
import math
import numpy as np


def func17(x):
    return x + 1 + math.exp(x)


def derv17(x):
    return 1 + math.exp(x)


def kosh17(x, y):
    return ((x+1) * derv17(x) - y) / x


a = 1
b = 2
h = 0.1
y0 = 2 + math.exp(1)
X = np.linspace(1, 2, int((b-a)/h)+1)


def euler(X, func, kosh, y, h):
    print("Метод Ейлера")
    Y = np.zeros(len(X))
    Y[0] = y
    emax = 0

    for i in range(1, len(Y)):
        Y[i] = Y[i-1] + kosh(X[i-1], Y[i-1]) * h

        eps = math.fabs(func(X[i]) - Y[i])
        if eps > emax:
            emax = eps

    print("x".ljust(5), "y".ljust(20), "eps".ljust(20))
    for i in range(0, len(Y)):
        print(str(round(X[i], 2)).ljust(5), str(Y[i]).ljust(
            20), str(math.fabs(func(X[i]) - Y[i])).ljust(20))
    print("Максимальна похибка:", emax)

    return X, Y


def euler_kosh(X, func, kosh, y, h):
    print("Метод Ейлера-Коші")
    Y = np.zeros(len(X))
    Y[0] = y
    emax = 0

    for i in range(1, len(Y)):
        yTemp = Y[i-1] + kosh(X[i-1], Y[i-1]) * h
        Y[i] = Y[i-1] + (kosh(X[i-1], Y[i-1]) + kosh(X[i], yTemp)) * h / 2

        eps = math.fabs(func(X[i]) - Y[i])
        if eps > emax:
            emax = eps

    print("x".ljust(5), "y".ljust(20), "eps".ljust(20))
    for i in range(0, len(Y)):
        print(str(round(X[i], 2)).ljust(5), str(Y[i]).ljust(
            20), str(math.fabs(func(X[i]) - Y[i])).ljust(20))
    print("Максимальна похибка:", emax)

    return X, Y


def rung_kut_mers(X, func, kosh, y, h):
    print("Метод Рунге-Кутта-Меросна")
    Y = np.zeros(len(X))
    Y[0] = y
    emax = 0

    for i in range(1, len(Y)):
        H3 = h/3
        K1 = H3 * kosh(X[i-1], Y[i-1])
        K2 = H3 * kosh(X[i-1] + H3, Y[i-1] + K1)
        K3 = H3 * kosh(X[i-1] + H3, Y[i-1] + (K1 + K2)/2)
        K4 = K1 + 4 * H3 * kosh(X[i-1] + h/2, Y[i-1] + 0.375 * (K1 + K3))
        K5 = H3 * kosh(X[i-1] + h, Y[i-1] + 1.5 * (K4 - K3))
        Y[i] = Y[i-1] + (K4 + K5) / 2

        eps = math.fabs(func(X[i]) - Y[i])
        if eps > emax:
            emax = eps

    print("x".ljust(5), "y".ljust(20), "eps".ljust(20))
    for i in range(0, len(Y)):
        print(str(round(X[i], 2)).ljust(5), str(Y[i]).ljust(
            20), str(math.fabs(func(X[i]) - Y[i])).ljust(20))
    print("Максимальна похибка:", emax)

    return X, Y


def adams(X, Y, func, kosh, y, h):
    print("Метод Адамса")
    emax = 0

    for i in range(4, len(Y)):
        Y[i] = Y[i-1] + h/24 * (55 * kosh(X[i-1], Y[i-1]) - 59 * kosh(
            X[i-2], Y[i-2]) + 37 * kosh(X[i-3], Y[i-3]) - 9 * kosh(X[i-4], Y[i-4]))

        eps = math.fabs(func(X[i]) - Y[i])
        if eps > emax:
            emax = eps

    print("x".ljust(5), "y".ljust(20), "eps".ljust(20))
    for i in range(0, len(Y)):
        print(str(round(X[i], 2)).ljust(5), str(Y[i]).ljust(
            20), str(math.fabs(func(X[i]) - Y[i])).ljust(20))
    print("Максимальна похибка:", emax)

    return X, Y


def adams_bash(X, func, kosh, y, h):
    print("Метод Адамса-Башфорта")
    Y = np.zeros(len(X))
    Y[0] = y
    emax = 0

    for i in range(5, len(Y)):
        Y[i-4] = Y[i-5] + h * kosh(X[i-5], Y[i-5])
        Y[i-3] = Y[i-4] + h * \
            (1.5 * kosh(X[i-4], Y[i-4]) - 0.5 * kosh(X[i-5], Y[i-5]))
        Y[i-2] = Y[i-3] + h * (23/12 * kosh(X[i-3], Y[i-3]) - 4 /
                               3 * kosh(X[i-4], Y[i-4]) + 5/12 * kosh(X[i-5], Y[i-5]))
        Y[i-1] = Y[i-2] + h * (55/24 * kosh(X[i-2], Y[i-2]) - 59/24 * kosh(
            X[i-3], Y[i-3]) + 37/24 * kosh(X[i-4], Y[i-4]) - 3/8 * kosh(X[i-5], Y[i-5]))
        Y[i] = Y[i-1] + h * (1901/720 * kosh(X[i-1], Y[i-1]) - 1387/360 * kosh(X[i-2], Y[i-2]) + 109 /
                             30 * kosh(X[i-3], Y[i-3]) - 637/360 * kosh(X[i-4], Y[i-4]) + 251/720 * kosh(X[i-5], Y[i-5]))

        eps = math.fabs(func(X[i]) - Y[i])
        if eps > emax:
            emax = eps

    print("x".ljust(5), "y".ljust(20), "eps".ljust(20))
    for i in range(0, len(Y)):
        print(str(round(X[i], 2)).ljust(5), str(Y[i]).ljust(
            20), str(math.fabs(func(X[i]) - Y[i])).ljust(20))
    print("Максимальна похибка:", emax)

    return X, Y


def adams_mult(X, Y, func, kosh, y, h):
    print("Метод Адамса-Мультона")
    emax = 0

    for i in range(4, len(Y)):
        Y[i] = Y[i-1] + h/24 * (55 * kosh(X[i-1], Y[i-1]) - 59 * kosh(
            X[i-2], Y[i-2]) + 37 * kosh(X[i-3], Y[i-3]) - 9 * kosh(X[i-4], Y[i-4]))
    for i in range(3, len(Y)):
        Y[i] = Y[i-1] + h/24 * (9 * kosh(X[i], Y[i]) + 19 * kosh(X[i-1],
                                                                 Y[i-1]) - 5 * kosh(X[i-2], Y[i-2]) + kosh(X[i-3], Y[i-3]))

        eps = math.fabs(func(X[i]) - Y[i])
        if eps > emax:
            emax = eps

    print("x".ljust(5), "y".ljust(20), "eps".ljust(20))
    for i in range(0, len(Y)):
        print(str(round(X[i], 2)).ljust(5), str(Y[i]).ljust(
            20), str(math.fabs(func(X[i]) - Y[i])).ljust(20))
    print("Максимальна похибка:", emax)

    return X, Y


xE, yE = euler(X, func17, kosh17, y0, h)
xEk, yEk = euler_kosh(X, func17, kosh17, y0, h)
xRkm, yRkm = rung_kut_mers(X, func17, kosh17, y0, h)
xA, yA = adams(X, yEk.copy(), func17, kosh17, y0, h)
xAb, yAb = adams_bash(X, func17, kosh17, y0, h)
xAm, yAm = adams_mult(X, yEk.copy(), func17, kosh17, y0, h)

y = np.exp(X) + X + 1
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(ylim=(4, 11), xlim=(0.9, 2.1))
ax.plot(X, y, color="black", label="e^x + x + 1", lw=1)
ax.plot(xE, yE, color="blue", label="euler", lw=1)
ax.plot(xEk, yEk, color="green", label="euler koshi", lw=1)
ax.plot(xRkm, yRkm, color="magenta", label="runge kutta mersona", lw=1)
ax.plot(xA, yA, color="aqua", label="adamsa", lw=1)
ax.plot(xAb, yAb, color="red", label="adamsa bashforta", lw=1)
ax.plot(xAm, yAm, color="orange", label="adamsa multona", lw=1)
plt.xticks([1 + h*i for i in range(int((b-a)/h) + 1)])
ax.legend(fontsize=16)
ax.grid(True)
plt.title("f(x) = e^x + x + 1", fontsize=20)
plt.tight_layout()
plt.show()
