import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftshift
from scipy.signal import argrelextrema
from numpy import array

def num1(letter:str='a'):
    def func(t:float, f:float=90):
        return np.sin(2*np.pi*f*t)

    if letter in ['a', 'b']:
        N = 200
        fs = 100
        df = fs/N
        trange = np.arange(N+1)/fs
        frange = np.arange(-N/2, N/2+1)*df
        X = func(trange)
        X = fft(X, N+1)
        X = fftshift(X)

        fig, ax = plt.subplots(1, 1, figsize=(12, 5))
        ax.plot(frange, np.abs(X), zorder=2)
        ax.set_xlabel('$f$')
        ax.set_ylabel('$|X|$')
        ax.set_xlim([frange[0], frange[-1]])
        ax.grid(zorder=1)

        if letter == 'b':
            ind_freqs = argrelextrema(np.abs(X), np.greater, order=2)
            print('Considering a one-side FFT')
            print('Frequency at peaks:')
            for freq in frange[ind_freqs][1:]:
                print(f'{freq:4.1f} Hz')
            ax.scatter(frange[ind_freqs], np.abs(X)[ind_freqs], c='r', zorder=3)

        plt.tight_layout()
        plt.show()

    elif letter in ['c', 'd', 'e']:
        if letter == 'c':
            print('The frequency signal it aliases is f=10Hz. We see no ' +
                'differences in both the magnitude of the peaks and at which ' +
                'frequencies they occur.')

        elif letter == 'd':
            print('The maximum frequency signal the FFT can represent for ' +
                'any sampling rate is half of the sampling rate/frequency. ' +
                'For the case of 100Hz being the sampling rate, the maximum ' +
                'would be 50Hz.')

        elif letter == 'e':
            print('Technically, no, the Nyquist criterion is not satisfied. ' +
                'We see that for frequencies greater than half the value of ' +
                'the sampling frequency, the FFT is an alias to another '+
                'signal. This tells us that the FFT of certain signals could ' +
                'accurately capture the FFT of the signal it is aliasing and ' +
                'could be used as a representation of that signal. However, ' +
                'technically, the Nyquist criterion is not satisfied in this ' +
                'case.')
        print()
        input('Press ENTER to exit.')

def num2(letter:str='a'):
    def func1(t:float, f:float=20, A:float=1):
        return A*np.sin(2*np.pi*f*t)

    def func2(t:float, f:float=30, A:float=10):
        return A*np.sin(2*np.pi*f*t)

    N = 200
    fs = 100
    df = fs/N
    trange = np.arange(N+1)/fs
    frange = np.arange(-N/2, N/2+1)*df

    if letter in ['a', 'b', 'c']:
        x = func1(trange) + func2(trange)
    elif letter == 'd':
        x = func1(trange, 30, 1) + func2(trange, 70, 1)

    fig, ax = plt.subplots(1, 1, figsize=(12, 5))
    if letter == 'a':
        ax.plot(trange, x, '.', c='C1', zorder=3)
        ax.plot(trange, x, zorder=2)
        ax.set_xlabel('$t$')
        ax.set_ylabel('$x$')
        ax.set_xlim([trange[0], trange[-1]])
        ax.grid(zorder=1)
        plt.tight_layout()
        plt.show()

    elif letter in ['b', 'c', 'd']:
        X = fft(x, N+1)
        X = fftshift(X)
        ind_freqs = argrelextrema(np.abs(X), np.greater, order=2)
        ax.scatter(frange[ind_freqs], np.abs(X)[ind_freqs], c='r', zorder=3)
        ax.plot(frange, np.abs(X), zorder=2)
        ax.set_xlabel('$f$')
        ax.set_ylabel('$|X|$')
        ax.set_xlim([frange[0], frange[-1]])
        ax.grid(zorder=1)

        if letter == 'b':
            print('Frequency at peaks:')
            for freq in frange[ind_freqs][2:]:
                print(f'{freq:4.1f} Hz')

        elif letter == 'c':
            print('It is evident from the plot that, in the frequency ' +
                'domain, f=30Hz has a larger peak.')

        elif letter == 'd':
            print('In this case, it is clear that there are numerous local ' +
                'peaks. However, there are still only two global peaks in ' +
                'the graph of the FFT.')

        plt.tight_layout()
        plt.show()

def num3(letter:str='a'):
    def func(t:float, N:int=5, f:float=1):
        X = 0
        for n in range(N):
            X += np.sin(2*np.pi*(2*n+1)*f*t) / (2*n+1)
        return 2/np.pi * X

    Ns = 200
    fs = 100
    df = fs/Ns
    trange = np.arange(Ns+1)/fs
    frange = np.arange(-Ns/2, Ns/2+1)*df

    if letter in ['a', 'c', 'd']:
        if letter == 'a':
            fig, ax = plt.subplots(3, 1, figsize=(12, 10))

            for i, N in enumerate([5, 10, 25]):
                X = func(trange, N)
                ax[i].plot(trange, X, '-', zorder=2)
                ax[i].set_xlabel('$t$')
                ax[i].set_ylabel('$x$')
                ax[i].set_xlim([trange[0], trange[-1]])
                ax[i].grid(zorder=1)
                ax[i].set_title(f'N = {N}')

        elif letter in ['c', 'd']:

            if letter == 'c':
                X = func(trange, 5)
            elif letter == 'd':
                X = func(trange, 10)

            X = fft(X, len(X))
            X = fftshift(X)
            #Xrange = np.arange(len(X))
            ind_freqs = argrelextrema(np.abs(X), np.greater, order=2)

            fig, ax = plt.subplots(1, 1, figsize=(12, 5))
            ax.scatter(frange[ind_freqs], np.abs(X)[ind_freqs], c='r', zorder=3)
            ax.plot(frange, np.abs(X), zorder=2)
            ax.set_xlabel('$f$')
            ax.set_ylabel('$|X|$')
            ax.set_xlim([frange[0], frange[-1]])
            ax.grid(zorder=1)

            if letter == 'c':
                freqs = frange[ind_freqs][5:]
                nums = ['1st', '2nd', '3rd', '4th']
                print('Considering a one-side FFT')
                print(f'Frequency of fundamental frequency: {freqs[0]:2.1f} Hz')
                for num, freq in zip(nums, freqs[1:]):
                    print(f'Frequency of {num} harmonic: {freq:2.1f} Hz')

            elif letter == 'd':
                print('The number of peaks are directly related to the ' +
                'number of harmonics. This means that increasing N would ' +
                'also increase the number of peaks.')

        plt.tight_layout()
        plt.show()

    elif letter == 'b':
        print('In all cases of N, there exists an overshoot at the ' +
            'discontinuities of the square wave. Increasing N does not ' +
            'remove this overshoot but merely moves it closer to the point ' +
            'of discontinuity. The overshoot is known as Gibbs phenomenon.')
        print()
        input('Press ENTER to exit.')

letters_cache = {
    '1':['a', 'b', 'c', 'd', 'e'],
    '2':['a', 'b', 'c', 'd'],
    '3':['a', 'b', 'c', 'd'],
}

functions_cache = {
    '1':num1,
    '2':num2,
    '3':num3
}

if __name__ == '__main__':
    numbers = list(range(1, 4))
    print(f'Choose a number in {numbers}')
    number = int(input('Number: ').strip())

    while number not in numbers:
        print('-'*30)
        print(f'ERROR: Number selected not in {numbers}')
        number = int(input('Number: ').strip())

    print('-'*30)
    letters = letters_cache[str(number)]
    print(f'Choose a letter in {letters}')
    letter = input('Letter: ').strip()
    while letter not in letters:
        print('-'*30)
        print(f'ERROR: Letter selected not in {letters}')
        letter = input('Letter: ').strip()

    print('-'*30)
    functions_cache[str(number)](letter)
