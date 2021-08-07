import numpy as np

def getPairs(F, interval, N=100):
    x = np.linspace(interval[0], interval[1], 100)
    y = F(x)

    ysign = np.sign(y)
    yroll = np.roll(ysign, 1); yroll[0] = yroll[1]
    ysign_change = ((yroll - ysign) != 0).astype(int)
    mask = np.roll(ysign_change, -1) + ysign_change

    Mx = x[mask == 1]
    My = y[mask == 1]

    xpairs = list(zip(Mx[::2], Mx[1::2]))
    ypairs = list(zip(My[::2], My[1::2]))

    return xpairs, ypairs

def bisection(F, xminus, xplus, max_iters=1000, eps=1e-6):

    for i in range(max_iters):
        x = (xplus + xminus) / 2
        if F(x) * F(xplus) > 0:
            xplus = x
        else:
            xminus = x
        if abs(F(x)) < eps:
            print(f'Root found with precision eps = {eps}')
            break
        if i == max_iters - 1:
            print(f'Root NOT found after Nmax iterations')

    return x

def automateSearch(F, interval, method='bisection', **kwargs):
    '''
    This method is faulty if F(interval[0]) = 0.
    Keep that in mind.
    '''
    roots = []
    xpairs, ypairs = getPairs(F, interval)

    for xpair, ypair in list(zip(xpairs, ypairs)):
        pair = list(zip(ypair, xpair)); pair.sort()
        xminus = pair[0][1]; xplus = pair[1][1]

        if method == 'bisection':
            root = bisection(F, xminus, xplus, **kwargs)

        roots.append(root)

    return roots

def secant_method(function, a, b, tol=np.finfo(float).eps):
    while True:
        x = b - function(b)*(b - a)/(function(b) - function(a))
        if abs(x - b) < tol:
            break
        a = b
        b = x
    return x
