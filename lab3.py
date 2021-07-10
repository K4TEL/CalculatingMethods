import matplotlib.pyplot as plt
import numpy as np

X17 = np.array([-2, -1, 0, 1, 2], dtype=float)
Y17 = np.array([-1.8647, -0.63212, 1, 3.7183, 9.3891], dtype=float)

xT = -0.5

def curv(x, y):
    n = len(x) - 1
    c = np.zeros((n), dtype=float)
    d = np.ones((n+1), dtype=float)
    e = np.zeros((n), dtype=float)
    k = np.zeros((n+1), dtype=float)
    
    c[0:n-1] = x[0:n-1] - x[1:n]
    d[1:n] = 2 * (x[0:n-1] - x[2:n+1])
    e[1:n] = x[1:n] - x[2:n+1]
    
    k[1:n] = 6 * (y[0:n-1] - y[1:n]) / (x[0:n-1] - x[1:n]) \
        -6 * (y[1:n] - y[2:n+1]) / (x[1:n] - x[2:n+1])
    
    n = len(d)
    for i in range(1, n):
        lam = c[i-1]/d[i-1]
        d[i] = d[i] - lam * e[i-1]
        c[i-1] = lam
        
    for i in range(1, n):
        k[i] = k[i] - c[i-1] * k[i-1]
    k[n-1] = k[n-1] / d[n-1]
    for j in range(n-2, -1, -1):
        k[j] = (k[j] - e[j] * k[j+1]) / d[j]
        
    return k

def spline(x, y, X):
    def seg(x, X):
        left = 0
        right = len(x) - 1
        while True:
            if (right - left) <= 1:
                return left
            i = int((left + right) / 2)
            if X < x[i]:
                right = i
            else:
                left = i
                
    k = curv(X17, Y17)
    i = seg(x, X)
    h = x[i] - x[i+1]
    Y = ((X - x[i+1])**3/h - (X - x[i+1])*h)*k[i]/6 \
        - ((X - x[i])**3/h - (X - x[i])*h)*k[i+1]/6 \
            + (y[i] * (X - x[i+1]) - y[i+1] * (X - x[i]))/h
    return Y

for i in range(len(X17)):
    print(str(X17[i]).rjust(4), str(Y17[i]).rjust(8))
print(xT, spline(X17, Y17, xT))

x = np.linspace(-2, 2, 1000)
y = [spline(X17, Y17, i) for i in x]
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(ylim=(-3, 10), xlim=(-3, 3))
plt.axvline(xT, color="red")
ax.plot(x, y, color="black", lw=2)
ax.plot(X17, Y17, "mo")
ax.plot(xT, spline(X17, Y17, xT), "ro")
ax.grid(True)
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")
plt.title("Spline", fontsize=20)
plt.show()
