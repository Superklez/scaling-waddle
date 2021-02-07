import numpy as np

def trapezoidal_rule(function, a, b, N=1000):
    f = function
    h = (b - a) / (N - 1)
    p = np.linspace(a, b, N)
    val = f(p[0])/2 + sum(f(p[1:-1])) + f(p[-1])/2
    return h * val

def simpsons_rule(function, a, b, N=999):
    if N % 2 == 0:
        print('N must be odd. Try again.')
        return
    f = function
    h = (b - a) / (N - 1)
    p = np.linspace(a, b, N)
    mask = np.arange(1, N-1)

    ends = f(p[0]) + f(p[-1])
    even = 2 * sum(f(p[1:-1][mask%2==0]))
    odd = 4 * sum(f(p[1:-1][mask%2==1]))

    return h/3 * (ends + even + odd)

def gaussian_quadrature(function, a, b, N=100):
    def gaussxw(N):
        a = np.linspace(3, 4*N-1, N) / (4*N + 2)
        x = np.cos(np.pi * a+ 1/(8 * N**2 *np.tan(a)))

        epsilon = np.finfo(float).eps
        delta = 1.0
        while delta > epsilon:
            p0 = np.ones(N)
            p1 = np.copy(x)
            for k in range(1, N):
                p0, p1 = p1, ((2 * k+1) * x*p1 - k*p0) / (k+1)
            dp = (N + 1) * (p0- x*p1) / (1 - x**2)
            dx = p1 / dp
            x -= dx
            delta = max(abs(dx))

        w = 2  *(N + 1) * (N + 1) / (N**2 * (1 - x**2) * dp**2)

        return x, w

    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w

    f = function
    solution = 0
    for i in range(len(x)):
        solution += wp[i] * f(xp[i])

    return solution

def monte_carlo_integration(function, a, b, N=1000, get_std=False):
    f = function
    h = b - a
    points = np.random.uniform(a, b, N)
    f_vals = f(points)
    mean = sum(f_vals) / N
    solution = h * mean
    if get_std:
        std_f = np.std(f_vals)
        std_I = std_f / np.sqrt(N)
        return solution, std_I
    return solution
