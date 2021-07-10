import math
import numpy as np

h = 0.2
a = 0.5
ya = 1
b = 1.5
yb = 0

def makeMatrix(X, h, p, q, f, yA, yB):
    N = X.shape[0] - 1
    Y = np.zeros([N, N])
    B = np.zeros(N)
    for i in range(N):
        if i == 0:
            Y[i, i] = (-2 + (h**2) * q(X[i]))
            Y[i, i+1] = (1 + h * p(X[i]) / 2)
            B[i] = (h**2) * f - (1 - h * p(X[i]) / 2) * yA
        elif i == N-1:
            Y[i, i] = 1/h + 1
            Y[i, i-1] = -1/h
            B[i] = yB
        else:
            Y[i, i] = (-2 + (h**2) * q(X[i]))
            Y[i, i-1] = (1 - h * p(X[i]) / 2)
            Y[i, i+1] = (1 + h * p(X[i]) / 2)
            B[i] = (h**2) * f
    return Y, B
        
def kinzriz(h, a, b, yA, yB):
    def fP(x):
        return -(2**x)

    def fQ(x):
        return -(x**2)
    
    X = np.linspace(a, b, int((b-a)/h)+1)
    A, B = makeMatrix(X, h, fP, fQ, -4, yA, yB)
    Y = np.linalg.solve(A, B)
    
    print("Кінцево-різницевий метод:")
    for row in range(len(B)):
        for col in range(len(A[row])):
            if A[row][col] > 0:
                print(" + ", end='')
            if A[row][col] < 0:
                print(" - ", end='')
            if A[row][col] == 0:
                print(" "*11, end='')
                continue
            print(str(round(math.fabs(A[row][col]), 4)).rjust(6), end='')
            print("y", end='')
            print(col+1, end='')
        print(" =", round(B[row], 4))
        
    print("i X   Y")
    for i in range(X.shape[0]):
        if i == 0:
            print(i, X[i], yA)
        else:
            print(i, X[i], Y[i-1])

print("y`` - 2^x * y` - x^2 * y + 4 = 0")
print("y(0.5) = 1")
print("y(1.5) + y`(1.5) = 0")
kinzriz(h, a, b, ya, yb)