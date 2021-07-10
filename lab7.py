import matplotlib.pyplot as plt
import math
import numpy as np

def FUNC_newt(X):
    return np.array([3*X[0] - math.cos(X[1]), 3*X[1] - math.exp(X[0])])

def JACOB(X):
    return np.array([[3, math.sin(X[1])], 
                     [math.exp(X[0]), 3]])

def FUNC_iter(X):
        return np.array([math.cos(X[1])/3, math.exp(X[0])/3])

def newton(func, jacob):
    X = np.array([0, 0], dtype=float)
    for it in range(10):
        J = jacob(X)
        Y = func(X)
        X = X - np.linalg.solve(J, Y)
    return X

def simpiter(func):
    X = np.array([0, 0], dtype=float)
    for it in range(10):
        X = func(X)
    return X

print("3x - cos(y) = 0")
print("3y - e^x = 0")
print("Метод Ньютона:", newton(FUNC_newt, JACOB))
print("Метод простих ітерацій:", simpiter(FUNC_iter))

x = np.linspace(0, 1/3, 1000)
y1 = np.exp(x)/3
y2 = np.arccos(3*x)
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(ylim=(0, 1))
ax.plot(x, y1, color="red", label="y = e^x / 3", lw=2)
ax.plot(x, y2, color="blue", label="y = arccos(3x)", lw=2)
ax.legend(fontsize=16)
ax.grid(True)
plt.title("3x - cos(y) = 0, 3y - e^x = 0", fontsize=20)
plt.show()