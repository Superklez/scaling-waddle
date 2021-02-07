import numpy as np

def secant_method(function, a, b, tol=np.finfo(float).eps):
    while True:
        x = b - function(b)*(b - a)/(function(b) - function(a))
        if abs(x - b) < tol:
            break
        a = b
        b = x
    return x
