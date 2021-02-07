import numpy as np

def forward_difference(function, t, h=1e-6):
    return (function(t + h) - function(t)) / h

def central_difference(function, t, h=1e-6, mode='half'):
    if mode == 'half':
        return (function(t + h / 2) - function(t - h / 2)) / h

    elif mode == 'quarter':
        return (function(t + h / 4) - function(t - h / 4)) / (h / 2)

def extrapolated_difference(function, t, h=1e-6):
    cd1 = CentralDifference(function, t, h, 'quarter')
    cd2 = CentralDifference(function, t, h, 'half')
    return (4 * cd1 - cd2) / 3

def higher_order_derivative(function, t, h=1e-6, order=2, method='cd'):
    def factorial(num):
        if num == 0:
            return 1

        for i in range(1, num):
            num *= i

        return num

    def binomial_coeff(n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))

    f = function
    numerator = []
    if method in ['fd', 'cd']:
        arg = order * h
        if method == 'cd':
            arg /= 2

        for i in range(order + 1):
            val = function(t + arg)
            coeff = binomial_coeff(order, i)
            if i % 2 != 0:
                coeff *= -1

            numerator.append(coeff * val)
            arg -= h

        return sum(numerator) / (h ** order)

    elif method == 'ed':
        print("This method is still unstable, please try using 'fd' or 'cd' instead.")
        return
        for arg in [h/4, h/2]:
            arg *= order - 1
            numerator.append(8*f(t + h/4 + arg) - 8*f(t - h/4 + arg) - f(t + h/2 + arg) + f(t - h/2 + arg))
            numerator.append(8*f(t + h/4 - arg) - 8*f(t - h/4 - arg) - f(t + h/2 - arg) + f(t - h/2 - arg))

        return sum(numerator) / ((3 * h) ** order)
