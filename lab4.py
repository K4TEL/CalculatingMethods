import matplotlib.pyplot as plt
import math
import numpy as np

def func17(x):
    return 1 / (256 - x**4)

aX = -2
bX = 2
h1 = 1.0
h2 = 0.5

def pram(a, b, h):
    m = int((b-a)/h)
    s = np.zeros(m)
    for i in range(m):
        x = a + i*h
        s[i] = s[i-1] + func17(x)*h
        #print(i,x, func17(x), s[i], s[i-1])
    return s[-1]

def trapez(a, b, h):   
    def trap(a, b, old, k):
        if k == 1:
            new = (func17(a) + func17(b))*(b - a)/2.0
        else:
            n = 2**(k-2)
            h = (b-a)/n
            x = a + h/2.0
            s = 0
            for i in range(n):
                s += func17(x)
                x += h
                new = (old + h*s)/2.0
        return new
    
    m = int((b-a)/h)
    old = 0.0    
    for k in range(1, int(math.log2(m) + 1)):
        new = trap(a, b, old, k)
        old = new
    return old
        
def simphson(a, b, h):
    m = int((b-a)/h)
    x = a
    s = 0
    se = 0
    so = 0
    for i in range(m):
        if i == 0 or i == m:
            s += func17(x)
        else:
            if i % 2 == 0:
                se += func17(x)
            else:
                so += func17(x)
        x += h
    return (h/3)*(s + 2*se + 4*so)
    
def runge_p(a, b, h1, h2, n):
    print("1. Метод прямокутників")
    eps = 10**-n
    I1 = pram(a, b, h1)
    I2 = pram(a, b, h2)
    print("Значення", I1, "за кроком", h1)
    print("Значення", I2, "за кроком", h2)
    delt = 1/3*math.fabs(I2 - I1)
    while delt > eps:
        #print( h1, h2, delt)
        h1 = h2
        h2 = h2/2.0
        I1 = pram(a, b, h1)
        I2 = pram(a, b, h2)
        delt = 1/3*math.fabs(I2 - I1)
    print("Точність:", eps, "Похибка:", delt, "за методом Рунге")
    print("Значення", I1, "за кроком", h1)
    print("Значення", I2, "за кроком", h2)
    return round(I1, n), round(I2, n)

def runge_t(a, b, h1, h2, n):
    print("2. Метод трапецій")
    eps = 10**-n
    I1 = trapez(a, b, h1)
    I2 = trapez(a, b, h2)
    print("Значення", I1, "за кроком", h1)
    print("Значення", I2, "за кроком", h2)
    delt = 1/3*math.fabs(I2 - I1)
    while delt > eps:
        #print( h1, h2, delt)
        h1 = h2
        h2 = h2/2.0
        I1 = trapez(a, b, h1)
        I2 = trapez(a, b, h2)
        delt = 1/3*math.fabs(I2 - I1)
    print("Точність:", eps, "Похибка:", delt, "за методом Рунге")
    print("Значення", I1, "за кроком", h1)
    print("Значення", I2, "за кроком", h2)
    return round(I1, n), round(I2, n)

def runge_s(a, b, h1, h2, n):
    print("3. Метод Сімпсона")
    eps = 10**-n
    I1 = simphson(a, b, h1)
    I2 = simphson(a, b, h2)
    print("Значення", I1, "за кроком", h1)
    print("Значення", I2, "за кроком", h2)
    delt = 1/15*math.fabs(I2 - I1)
    while delt > eps:
        #print( h1, h2, delt)
        h1 = h2
        h2 *= 0.5
        I1 = simphson(a, b, h1)
        I2 = simphson(a, b, h2)
        delt = 1/15*math.fabs(I2 - I1)
    print("Точність:", eps, "Похибка:", delt, "за методом Рунге")
    print("Значення", I1, "за кроком", h1)
    print("Значення", I2, "за кроком", h2)
    return round(I1, n), round(I2, n)
        
def romb(inter, a, b, h, m):
    eps = 10**-m
    print("Точність:", eps, "за методом Ромберга")
    r = np.array([[0] * (m+1)] * (m+1), float)
    h = b-a
    r[0, 0] = inter(a, b, h)
    power = 1
    for i in range(1, m + 1):
        h *= 0.5
        s = 0
        power *= 2
        for k in range(1, power, 2):
            s += func17(a + k*h)
        r[i, 0] = 0.5 * r[i-1, 0] + s*h
        power4 = 1
        for j in range(1, i+1):
            power4 *= 4
            r[i, j] = r[i, j-1] + (r[i, j-1] - r[i-1, j-1])/(power4 - 1)
    print("Значення", r[-1][-1], "за кроком", h)
    return r[-1][-1]
        
    

x = np.linspace(-3, 3, 1000)
X = np.linspace(-2, 2, 1000)
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(ylim=(-0.001, 0.006), xlim=(-3, 3))
ax.plot(x, 1 / (256 - x**4), color="black", label="1 / (256 - x^4)", lw=3)
plt.axvline(-2, color="#f3c616", lw=3)
plt.axvline(2, color="#f3c616", lw=3)
plt.fill_between(X, 1 / (256 - X**4), 0, color="#f3c616", alpha=.7)
ax.legend()
ax.grid(True)
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")
plt.title("f(x) = 1 / (256 - x^4);   a = -2;  b = 2;", fontsize=20)
plt.show()

H1 = []
H2 = []
H1r = []
H2r = []
H1rr = []
H2rr = []

H1.append(pram(aX, bX, h1))
H2.append(pram(aX, bX, h2))
i1, i2 = runge_p(aX, bX, h1, h2, 8)
H1r.append(i1)
H2r.append(i2)
H1rr.append(romb(pram, aX, bX, h1, 8))
H2rr.append(romb(pram, aX, bX, h2, 8))

H1.append(trapez(aX, bX, h1))
H2.append(trapez(aX, bX, h2))
i1, i2 = runge_t(aX, bX, h1, h2, 8)
H1r.append(i1)
H2r.append(i2)
H1rr.append(romb(trapez, aX, bX, h1, 8))
H2rr.append(romb(trapez, aX, bX, h2, 8))

H1.append(simphson(aX, bX, h1))
H2.append(simphson(aX, bX, h2))
i1, i2 = runge_s(aX, bX, h1, h2, 8)
H1r.append(i1)
H2r.append(i2)
H1rr.append(romb(simphson, aX, bX, h1, 8))
H2rr.append(romb(simphson, aX, bX, h2, 8))




barWidth = 0.15
r1 = np.arange(len(H1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
fig, ax = plt.subplots()
fig.set_size_inches(10, 10)
ax.grid(axis="y")
ax.set(ylim=[0.014, 0.0165])
ax.xaxis.tick_top()
plt.xticks([r + 3*barWidth for r in range(len(H1))],
           ["Прямокутників", "Трапецій", "Сімпсона"], fontsize=16)
plt.bar(r1, H1, color="#df343c", width=barWidth, label="H1")
plt.bar(r2, H2, color="#f3c616", width=barWidth, label="H2")
plt.bar(r3, H1r, color="#6fb90e", width=barWidth, label="H1 Runge")
plt.bar(r4, H2r, color="#0ddec5", width=barWidth, label="H2 Runge")
plt.bar(r5, H1r, color="#3172e3", width=barWidth, label="H1 Romberg")
plt.bar(r6, H2r, color="#ac2adf", width=barWidth, label="H2 Romberg")
plt.title("h1 = 1.0; h2 = 0.5;", fontsize=20)
plt.legend()
plt.show()