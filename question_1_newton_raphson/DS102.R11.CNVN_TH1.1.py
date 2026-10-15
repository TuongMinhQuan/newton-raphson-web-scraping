import numpy as np

def f(x):
    return 3 * x[0]**2 - 2 * x[1]**2 - 3 * x[0] - 5 * x[1]

def gradient(x):
    return np.array([6 * x[0] - 3, - 4 * x[1] - 5])

def hessian(x):
    return np.array([[6, 0], [0, -4]])

def newton_raphson(x0, epsilon=1e-10):
    x = x0.astype(float)

    while True:
        grad = gradient(x)
        hess = hessian(x)

        delta = np.linalg.solve(hess, grad)
        x_new = x - delta

        if np.linalg.norm(x_new - x) < epsilon:
            break

        x = x_new

    return x_new


x0 = np.array([0.0, 0.0])

result = newton_raphson(x0)

print("Diem dung:", result)
print("Gia tri f:", f(result))