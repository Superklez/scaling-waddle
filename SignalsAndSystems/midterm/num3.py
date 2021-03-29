import numpy as np
import matplotlib.pyplot as plt

def main(wc:float, num:int=1000):
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

if __name__ == '__main__':
    wc = float(input('Cut-off frequency wc: ').strip())
    main(wc)
