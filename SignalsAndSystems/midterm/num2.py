import numpy as np
import matplotlib.pyplot as plt

def main(n=1000, nmax:int=20, minmax:list=None):
    def func(t):
        T0 = 2*np.pi; w0 = 2*np.pi/T0
        return 1/4 + sum(np.cos(nrnge*t)*(np.cos(nrnge*np.pi)-1)/nrnge**2/
            np.pi**2) - sum(np.sin(nrnge*t)*np.cos(nrnge*np.pi)/nrnge/np.pi)
    if minmax:
        a, b = minmax
    else:
        a, b = -3*np.pi, 3*np.pi
    arr = np.linspace(a, b, n); crr = np.zeros(arr.shape)
    rnge = np.arange(0.,b+1,np.pi)
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
    fig, ax = plt.subplots(1, 1, figsize=(7,5))
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

if __name__ == '__main__':
    main()
