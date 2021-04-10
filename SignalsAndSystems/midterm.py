import numpy as np
import matplotlib.pyplot as plt

def num1(T:float, nmax:int=20, num:int=1000, minmax:list=None):
    def func(t):
        T0 = T; w0 = 2*np.pi/T0
        return 4/np.pi * sum(np.sin(nrnge*w0*t)/nrnge)
    if minmax:
        a, b = minmax
    else:
        a, b = -T, T
    arr = np.linspace(a, b, num)
    crr = -np.ones(arr.shape)
    rnge = np.arange(0, b+1, T/2)
    nrnge = np.arange(1, nmax, 2)
    trnge = np.linspace(a, b, 1000)
    ts = [func(t) for t in trnge]
    for x in rnge[::2]:
        crr[(x <= arr) & (arr <= x+T/2)] = 1
        crr[(-(x+T) <= arr) & (arr <= -(x+T/2))] = 1
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
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

def num2(n:int=1000, nmax:int=20, minmax:list=None):
    def func(t):
        T0 = 2*np.pi; w0 = 2*np.pi/T0
        return 1/4 + sum(np.cos(nrnge*t)*(np.cos(nrnge*np.pi)-1)/nrnge**2/
            np.pi**2) - sum(np.sin(nrnge*t)*np.cos(nrnge*np.pi)/nrnge/np.pi)
    if minmax:
        a, b = minmax
    else:
        a, b = -3*np.pi, 3*np.pi
    arr = np.linspace(a, b, n); crr = np.zeros(arr.shape)
    rnge = np.arange(0., b+1, np.pi)
    nrnge = np.arange(1, nmax); trnge = np.linspace(a, b, 1000)
    ts = [func(t) for t in trnge]
    for x in rnge[::2]:
        shp1 = crr[(x <= arr) & (arr <= x+np.pi)].shape[0]
        shp2 = crr[(-(x+2*np.pi) <= arr) & (arr <= -(x+np.pi))].shape[0]
        try:
            crr[(x <= arr) & (arr <= x+np.pi)] = arr[
                (0 <= arr) & (arr <= np.pi)][:shp1]/np.pi
            crr[(-(x+2*np.pi) <= arr) & (arr <= -(x+np.pi))] = arr[
                (0 <= arr) & (arr <= np.pi)][-shp2:]/np.pi
        except:
            pass
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    xticks = np.concatenate([-rnge[::-1][:-1], rnge])
    xticklabels = ['0']
    for i in range(1, len(rnge)):
        if i == 1:
            xticklabels += ['$\pi$']
        else:
            xticklabels += [f'${i}\pi$']
    for i in range(1, len(rnge)):
        if i == 1:
            xticklabels.insert(0, '$-\pi$')
        else:
            xticklabels.insert(0, f'$-{i}\pi$')
    ax.plot(trnge, ts, zorder=4)
    ax.step(arr, crr, zorder=3)
    ax.set_xlabel('$t$'); ax.set_ylabel('$f(t)$')
    ax.set_xticks(xticks); ax.set_xticklabels(xticklabels)
    ax.axhline(y=0, color='k', zorder=2); ax.axvline(x=0, color='k', zorder=2)
    ax.set_xlim([a, b])
    ax.grid(zorder=1)
    plt.tight_layout()
    plt.show()

def num3(wc:float, num:int=1000):
    Ns = [1, 7, 19]
    W = np.linspace(-np.pi, np.pi, num)
    def func(w):
        return wc/np.pi + 2*sum(
            np.sin(wc*nrnge)/(np.pi*nrnge)*np.cos(w*nrnge))
    fig, ax = plt.subplots(1, 3, figsize=(17, 5))
    for i, N in enumerate(Ns):
        nrnge = np.arange(1, N+1)
        ws = [func(w) for w in W]
        ax[i].plot(W, ws, zorder=3)
        ax[i].set_xticks([-np.pi, -wc, 0, wc, np.pi])
        ax[i].set_yticks(np.linspace(0, 1, 6))
        ax[i].set_xticklabels(['$-\pi$', '$-w_c$', '$0$', '$w_c$', '$\pi$'])
        ax[i].set_xlabel('Angular frequency ($\omega$)')
        ax[i].set_ylabel('$H_N(\omega)$')
        ax[i].axhline(y=0, color='k', zorder=2)
        ax[i].axvline(x=0, color='k', zorder=2)
        ax[i].set_xlim([-np.pi, np.pi])
        ax[i].set_title(f'N = {N}')
        ax[i].grid(True, zorder=1)
    plt.tight_layout()
    plt.show()

def num4(a:float=0.5, num:int=1000, minmax:list=None):
    if minmax:
        start, stop = minmax
        w = np.linspace(start, stop, n)
    else:
        w = np.linspace(-np.pi, np.pi, num)
    z = 1/(1-a*(np.cos(w)-1j*np.sin(w)))
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for i, z in enumerate([z.real, z.imag]):
        ax[i].plot(w, z, zorder=3)
        ax[i].axhline(y=0, color='k', zorder=2)
        ax[i].axvline(x=0, color='k', zorder=2)
        ax[i].set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
        ax[i].set_xticklabels(['$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'])
        ax[i].set_xlabel('Angular frequency ($\omega$)')
        ax[i].set_ylabel('Amplitude')
        ax[i].set_xlim([-np.pi, np.pi])
        ax[i].grid()
        if i == 0:
            ax[i].set_title('Real part')
        elif i == 1:
            ax[i].set_title('Imaginary part')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    number = int(input(f'Choose a number in {list(range(1, 5))}: ').strip())

    while number not in range(1, 5):
        print('-'*45)
        print(f'ERROR: Number provided not in {list(range(1, 5))}')
        number = int(input(f'Choose a number in {list(range(1, 5))}: ').strip())

    print('-'*45)
    print(f'Selected number: {number}')

    if number == 1:
        T = float(input('Fundamental period T: ').strip())
        num1(T)
    elif number == 2:
        num2()
    elif number == 3:
        wc = float(input('Cut-off frequency wc: ').strip())
        num3(wc)
    elif number == 4:
        num4()
