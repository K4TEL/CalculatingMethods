import matplotlib.pyplot as plt
import math
import numpy as np

def func17(x):
    return 4**x - 5*x - 2

def der17(x):
    return (4**x)*math.log(4) - 5

def lin17_1(x):
    return math.log(5*x + 2, 4)

def lin17_2(x):
    return (4**x - 2)/5

xGorb = math.log(5/math.log(4), 4)

def interval(a, b, n):
    eps = 10**-n
    x1 = a
    y1 = func17(x1)
    for x2 in range(a+1, b+1):
        y2 = func17(x2)
        if y1 * y2 > 0:
            y1 = y2
            x1 = x2
        else:
            break
    xRes = [x1, x2]
    print("Проміжок для пошуку кореня:", xRes, "з точністю до", eps)
    return xRes, eps

def poldil(a, b, n):
    xRes, eps = interval(a, b, n)

    while xRes[1] - xRes[0] > eps:
        xS = (xRes[0]+xRes[1])/2.0
        if func17(xS) * func17(xRes[0]) > 0:
            xRes[0] = xS
        else:
            xRes[1] = xS
            
    print("Проміжок x координати:", xRes)
    yRes = [func17(xRes[0]), func17(xRes[1])]
    print("Проміжок y координати:", yRes)
    return round(xS, n), round(func17(xS), n)

def newton(a, b, n):
    xRes, eps = interval(a, b, n)
    
    x = xRes[0]
    h = func17(x)/der17(x)
    while math.fabs(h) > eps:
        h = func17(x)/der17(x)
        x -= h
    
    print("Наближення на", h, "при похідній", der17(x))
    return round(x, n), round(func17(x), n)
        
def simpiter_1(a, b, n):
    xRes, eps = interval(a, b, n)
    
    xS = (xRes[0] + xRes[1])/2.0
    x = lin17_1(xS)
    while math.fabs(x - xS) >= eps:
        xS = x
        x = lin17_1(x)
        
    print("Значення x = math.log(5*x + 2, 4) подання:", lin17_1(x))
    return round(x, n), round(func17(x), n)

def simpiter_2(a, b, n):
    xRes, eps = interval(a, b, n)
    
    xS = (xRes[0] + xRes[1])/2.0
    x = lin17_2(xS)
    while math.fabs(x - xS) >= eps:
        xS = x
        x = lin17_2(x)
        
    print("Значення x = (4**x - 2)/5 подання:", lin17_2(x))
    return round(x, n), round(func17(x), n)

def graph(x1, y1, x2, y2, clr, ttl):
    x = np.linspace(-5, 5, 1000)
    fig = plt.figure(figsize=(10, 10))
    ax = plt.subplot(ylim=(-3, 2), xlim=(-1, 2))
    ax.plot(x, 4**x - 5*x - 2, color="black", lw=3)
    ax.plot(x1, y1, clr[0]+"o")
    ax.plot(x2, y2, clr[0]+"o")
    ax.grid(True)
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    plt.title(ttl , fontsize=20)
    plt.axvline(x1, color=clr)
    plt.axvline(x2, color=clr)
    plt.show()
    
print(xGorb, func17(xGorb))
x = np.linspace(-5, 5, 1000)
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(ylim=(-5, 16), xlim=(-5, 5))
ax.plot(x, 4**x - 5*x - 2, color="black", label="4^x - 5x - 2", lw=3)
ax.plot(x, 4**x, color="green", label="4^x", lw=2)
ax.plot(x, 5*x + 2, color="green", label="5x + 2", lw=2)
ax.plot(x, (4**x)*math.log(4) - 5, color="gray", label="(4^x)ln4 - 5")
ax.plot(xGorb, func17(xGorb), "yo")
ax.plot(xGorb, 0, "yo")
plt.axvline(xGorb, color="yellow")
ax.legend()
ax.grid(True)
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")
plt.title("4^x - 5x - 2 = 0", fontsize=20)
plt.show()

x1, y1 = poldil(-10, int(xGorb), 4)
print("Корінь x1:", x1, y1)
x2, y2 = poldil(int(xGorb), 10, 4)
print("Корінь x2:", x2, y2)
graph(x1, y1, x2, y2, "red", "Метод половинного ділення")

x1, y1 = newton(-10, int(xGorb), 4)
print("Корінь x1:", x1, y1)
x2, y2 = newton(int(xGorb), 10, 4)
print("Корінь x2:", x2, y2)
graph(x1, y1, x2, y2, "blue", "Метод Ньютона")

x1, y1 = simpiter_2(-10, int(xGorb), 4)
print("Корінь x1:", x1, y1)
x2, y2 = simpiter_1(int(xGorb), 10, 4)
print("Корінь x2:", x2, y2)
graph(x1, y1, x2, y2, "green", "Метод простої ітерації")