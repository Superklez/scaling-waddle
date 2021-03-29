import numpy as np
import matplotlib.pyplot as plt

def main(a:float=0.5, num:int=1000, minmax:list=None):
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
    main()
