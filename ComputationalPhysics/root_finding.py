import numpy as np
import matplotlib.pyplot as plt
#from utils.roots import secant_method

def secant_method(function, a, b, tol=np.finfo(float).eps):
    while True:
        x = b - function(b)*(b - a)/(function(b) - function(a))
        if abs(x - b) < tol:
            break
        a = b
        b = x
    return x

def func(x):
    return x**3 - 3*x**2 - 144*x + 432

x = np.linspace(-20, 20, 1000)
y = func(x)

x1 = secant_method(func, -15, -10)
x2 = secant_method(func, 0, 5)
x3 = secant_method(func, 10, 15)

print(f'First root (x1): {x1}')
print(f'Second root (x2): {x2}')
print(f'Third root (x3): {x3}')

plt.figure(dpi=100)
plt.grid(True)
plt.axhline(0, c='black')
plt.axvline(0, c='blacK')
plt.ylim((-1500, 1500))
plt.xticks([-20, -15, x1, -10, -5, 0, x2, 5, 10, x3, 15, 20])

plt.plot(x, y, zorder=2)
plt.scatter(x1, 0, c='C1', label='$x_1$', zorder=3)
plt.scatter(x2, 0, c='C2', label='$x_2$', zorder=3)
plt.scatter(x3, 0, c='C3', label='$x_3$', zorder=3)
plt.legend(loc='best')
plt.tight_layout()
plt.show()
