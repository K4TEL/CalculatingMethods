import math
import numpy as np

mat1 = [[8, 8, -5, -8],
        [8, -5, 9, -8],
        [5, -4, -6, -2],
        [8, 3, 6, 6]]
stolb1 = [13, 38, 14, -95]

mat2 = [[-6, 5, 0, 0, 0],
        [-1, 13, 6, 0, 0],
        [0, -9, -15, -4, 0],
        [0, 0, -1, -7, 1],
        [0, 0, 0, 9, -18]]
stolb2 = [51, 100, -12, 47, -90]

mat3 = np.array([[-19, 2, -1, -8],
        [2, 14, 0, -4],
        [6, -5, -20, -6],
        [-6, 4, -2, 15]], dtype=float)
stolb3 = np.array([38, 20, 52, 43], dtype=float)

def printSLAR(A, B):
    for row in range(len(B)):
        for col in range(len(A[row])):
            if A[row][col] > 0:
                print(" + ", end='')
            if A[row][col] < 0:
                print(" - ", end='')
            if A[row][col] == 0:
                print("      ", end='')
                continue
            print(int(math.fabs(A[row][col])), end='')
            print("x", end='')
            print(col+1, end='')
        print(" =", B[row])
            
def gauss(A, B):
    def swapRows(A, B, i1, i2):
        A[i1], A[i2] = A[i2], A[i1]
        B[i1], B[i2] = B[i2], B[i1]
        
    def divRow(A, B, i, div):
        A[i] = [a/div for a in A[i]]
        B[i] = B[i]/div 
        
    def combRows(A, B, i1, i2, weight):
        A[i1] = [(a + k*weight) for a, k in zip(A[i1], A[i2])]
        B[i1] += B[i2] * weight

    column = 0
    while (column < len(B)):
        row = None
        for r in range(column, len(A)):
            if row is None or math.fabs(A[r][column]) > math.fabs(A[row][column]):
                row = r
                
        if row != column:
            swapRows(A, B, row, column)
        divRow(A, B, column, A[column][column])
        for r in range(column + 1, len(A)):
            combRows(A, B, r, column, -A[r][column])
            
        column += 1
    
    X = [0 for b in B]
    for i in range(len(B)-1, -1, -1):
        X[i] = int(B[i] - sum(x * a for x, a in zip(X[(i+1):], A[i][(i+1):])))
        
    return np.array(X, dtype=float)

def progon(A, B):
    n = len(B)
    U, M, D = [], [], [0]
    for i in range(n):
        M.append(A[i][i])
        if i < n-1:
            U.append(A[i][i+1])
        if i > 0:
            D.append(A[i][i-1])
            
    a, b = [], []
    for i in range(n):
        if i == 0:
            a.append(-U[i] / M[i])
            b.append(B[i] / M[i])
        else:
            y = M[i] + D[i] * a[i-1]
            b.append((B[i] - D[i] * b[i-1]) / y)
            if i != n-1:
                a.append(-U[i] / y)
                
    X = [0] * n
    X[-1] = int(b[-1])
    for i in reversed(range(n-1)):
        X[i] = int((a[i] * X[i+1] + b[i]))
    return np.array(X, dtype=float)
    
def simpiter(A, B):
    n = B.shape[0]
    X = np.zeros_like(B)
    for it in range(100):
        x = np.zeros_like(X)
        for i in range(n):
            s = 0
            for j in range(n):
                if j!= i:
                    s += A[i, j]/A[i,i] * X[j]
            x[i] = B[i] / A[i,i] - s
        X = x
    return X

def seidel(A, B):
    X = np.zeros_like(B)
    while True:
        x = np.copy(X)
        for i in range(B.shape[0]):
            s1 = np.dot(A[i, :i], X[:i])
            s2 = np.dot(A[i, i+1:], X[i+1:])
            x[i] = (B[i] - s1 - s2) / A[i, i]
        if np.allclose(X, x, atol=1e-10, rtol=0.):
            break
        X = x
    return X
    

printSLAR(mat1, stolb1)
print("Точний розв'язок:", np.linalg.solve(mat1, stolb1))
print("Метод Гауса:", gauss(mat1, stolb1))

printSLAR(mat2, stolb2)
print("Точний розв'язок:", np.linalg.solve(mat2, stolb2))
print("Метод Прогонки:", progon(mat2, stolb2))

printSLAR(mat3, stolb3)
print("Точний розв'язок:", np.linalg.solve(mat3, stolb3))
print("Метод Простих ітерацій:", simpiter(mat3, stolb3))
print("Метод Зейделя:", seidel(mat3, stolb3))