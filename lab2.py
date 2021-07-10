import matplotlib.pyplot as plt
import math
import numpy as np

def func17(x):
    return math.exp(x) + x

dipX1 = [-2, -1, 0, 1]
dipX2 = [-2, -1, 0.2, 1]
tX = -0.5

def lagranj(dipX, dipY, x):
    z = 0
    for j in range(len(dipY)):
        p1 = 1
        p2 = 1
        for i in range(len(dipX)):
            if i == j:
                p1 *= 1
                p2 *= 1
            else:
                p1 *= x - dipX[i]
                p2 *= dipX[j] - dipX[i]
        z += dipY[j] * p1 / p2
    return z

def lagranDraw(X, clr):
    nX = np.linspace(-3, 3, 1000)
    Y = np.exp(nX) + nX
    x = np.array(X, dtype=float)
    y = np.array([func17(x) for x in X], dtype=float)
    
    newX = np.linspace(np.min(x), np.max(x), 1000)
    newY = [lagranj(x, y, i) for i in newX]
    
    fig = plt.figure(figsize=(10, 10))
    ax = plt.subplot(ylim=(-3, 4), xlim=(-3, 2))
    plt.axvline(tX, color="yellow")
    ax.plot(tX, lagranj(x, y, tX), "yo", markersize=10)
    ax.plot(x, y, clr[0] + "o")
    ax.plot(nX, Y, color="black", lw=1)
    ax.plot(newX, newY, color=clr, lw=3)
    ax.grid(True)
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    plt.title("Лагранжа " + str(X), fontsize=20)
    plt.show()
    
def coef(X):
    x = np.array(X, dtype=float)
    y = np.array([func17(x) for x in X], dtype=float)
    m = len(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])
    return a

def evalN(a, dipX, x):
    X = np.array(dipX, dtype=float)
    n = len(a) - 1
    y = a[n]
    for i in range(1, n+1):
        y = a[n-i] + y * (x - X[n-i])
    return y

def newtonDraw(X, clr):
    a = coef(X)
    nX = np.linspace(-3, 3, 1000)
    Y = np.exp(nX) + nX
    newX = np.linspace(np.min(X), np.max(X), 1000)
    newY = [evalN(a, X, i) for i in newX]
    
    fig = plt.figure(figsize=(10, 10))
    ax = plt.subplot(ylim=(-3, 4), xlim=(-3, 2))
    plt.axvline(tX, color="yellow")
    ax.plot(tX, evalN(a, X, tX), "yo", markersize=10)
    ax.plot(X, [func17(x) for x in X], clr[0] + "o")
    ax.plot(nX, Y, color="black", lw=1)
    ax.plot(newX, newY, color=clr, lw=3)
    ax.grid(True)
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    plt.title("Ньютона " + str(X), fontsize=20)
    plt.show()
    
x = np.linspace(-10, 10, 1000)
y = np.exp(x) + x
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(ylim=(-3, 4), xlim=(-3, 2))
ax.plot(x, y, color="black", label="e^x + x", lw=3)
ax.legend()
ax.grid(True)
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")
plt.title("f(x) = e^x + x", fontsize=20)
plt.show()

lagranDraw(dipX1, "red")
lagranDraw(dipX2, "blue")

newtonDraw(dipX1, "green")
newtonDraw(dipX2, "magenta")

data = [func17(tX)]
print(data[0], "за функцією")
for dip in [dipX1, dipX2]:
    y = lagranj(dip, [func17(x) for x in dip], tX)
    data.append(y)
    print(y, "за Лагранжа з похибкою", math.fabs(func17(tX)-y))
    
for dip in [dipX1, dipX2]:
    a = coef(dip)
    y = evalN(a, dip, tX)
    data.append(y)
    print(y, "за Ньютона з похибкою", math.fabs(func17(tX)-y))
    
x = np.linspace(-10, 10, 1000)
y = np.exp(x) + x
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(ylim=(0, 0.2), xlim=(-1, 0))
clr = "yrbgm"
names = ["Оригінал", "Лагранж Х1", "Лагранж Х2", "Ньютон Х1", "Ньютон Х2"]
plt.axvline(tX, color="yellow")
for i, Y in enumerate(data):
    ax.plot(tX, Y, clr[i] + "o", label = str(Y) + " " + names[i])
ax.legend(fontsize=16)
ax.grid(True)
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")
plt.show()