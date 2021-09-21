import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

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

def gaussian_quadrature(function, a, b, N=100):
    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w

    f = function
    solution = 0
    for i in range(len(x)):
        solution += wp[i] * f(xp[i])

    return solution
    
def integral(x):
    return (15 / const.pi**4) * (x**3) / (np.exp(x) - 1)

def eta(T, N=100):
    lambda_1 = 380 # in nm
    lambda_2 = 700 # in nm

    # Planck constant: const.h == 6.62607015e-34 J/Hz
    # Speed of light: const.c == 299792458.0 m/s
    # Boltzmann constant: const.k == 1.380649e-23 J/K

    lower_bound = const.h * (const.c * 1e9) / (lambda_2 * const.k) # Kelvin
    upper_bound = const.h * (const.c * 1e9) / (lambda_1 * const.k) # Kelvin

    return gaussian_quadrature(integral, lower_bound / T, upper_bound / T, N)

def golden_ratio_search(x1, x4, acc=1):
    """
    This is a slight modification of the golden ratio search, where we take
    the negative of the function outputs. This is necessary because the eta
    function being used returns a positive value, and the golden ratio search
    searches for the minima.
    """
    x2 = x4 - (x4 - x1) / const.golden_ratio
    x3 = x1 + (x4 - x1) / const.golden_ratio
    
    f1 = eta(x1)
    f2 = eta(x2)
    f3 = eta(x3)
    f4 = eta(x4)
    
    while (x4 - x1) > acc:
        if f2 > f3 :
            x4, f4 = x3, f3
            x3, f3 = x2, f2
            x2 = x4 - (x4 - x1) / const.golden_ratio
            f2 = eta(x2)

        else:
            x1, f1 = x2, f2
            x2, f2 = x3, f3
            x3 = x1 + (x4 - x1) / const.golden_ratio
            f3 = eta(x3)
            
    return 0.5 * (x2 + x3)

def main():
    T_min = 850     # in Kelvin
    T_max = 10000   # in Kelvin
    N = 100         # number of points for precision

    T = np.linspace(T_min, T_max, N)
    etas = list(map(eta, T))

    temp_max_eff = golden_ratio_search(6000, 8000, 1e-9)
    eta_max_eff = eta(temp_max_eff)

    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.plot(T, etas, zorder=2)
    ax.scatter(temp_max_eff, eta_max_eff, c='r', zorder=3)
    ax.grid(True, zorder=1)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Efficiency $\eta$")
    plt.show()

if __name__ == "__main__":
    main()