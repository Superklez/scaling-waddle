import numpy as np
import matplotlib.pyplot as plt

def main(T:float, nmax:int=20, num:int=1000, minmax:list=None):
    def func(t):
        T0 = T; w0 = 2*np.pi/T0
        return 4/np.pi * sum(np.sin(nrnge*w0*t)/nrnge)
    if minmax:
        a, b = minmax
    else:
        a, b = -T, T
    arr = np.linspace(a, b, num)
    crr = -np.ones(arr.shape)
    rnge = np.arange(0,b+1,T/2)
    nrnge = np.arange(1, nmax, 2)
    trnge = np.linspace(a, b, 1000)
    ts = [func(t) for t in trnge]
    for x in rnge[::2]:
        crr[(x <= arr) & (arr <= x+T/2)] = 1
        crr[(-(x+T) <= arr) & (arr <= -(x+T/2))] = 1
    fig, ax = plt.subplots(1, 1, figsize=(7,5))
    xticks = [-x for x in rnge[1:][::-1]]
    xticks += [x for x in rnge]
    ax.plot(trnge, ts, zorder=4)
    ax.step(arr, crr, zorder=3)
    ax.set_xlabel('$t$')
    ax.set_ylabel('$f(t)$')
    ax.set_xticks(xticks)
    ax.set_xlim([a, b])
    ax.axhline(y=0, color='k', zorder=2)
    ax.axvline(x=0, color='k', zorder=2)
    ax.grid(zorder=1)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    T = float(input('Fundamental period T: ').strip())
    main(T)
